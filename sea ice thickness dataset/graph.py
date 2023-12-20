import os
import xarray as xr
import copernicus_marine_client as copernicusmarine

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import *
from tensorflow.keras import Sequential
from tensorflow.keras.regularizers import l1_l2
import keras_tuner


# Download data from source website form two dataset_id
copernicusmarine.login("xfeng4","Sf1260358662@") #login, overwrite it ? [y/N]: y

#field name in dataset
data_variables = ["sithick","siconc","thetao","bottomT","so", "usi", "vsi","uo","vo"]

#create folder to store raw data
cwd = os.getcwd()
folder = "sea ice thickness dataset"
site = "greenland" #create dictionary: {site: lat and long range}
folder_path = os.path.join(cwd, folder, site)
os.makedirs(folder_path, exist_ok=True)

# first dataset
for var in data_variables:
    output_file = os.path.join(folder_path, f"{var}_id1.nc")
    if os.path.exists(output_file):
        pass
    else:
        copernicusmarine.subset(
            dataset_id="cmems_mod_glo_phy_my_0.083deg_P1D-m",
            variables=[var],
            minimum_longitude=-58.133,
            maximum_longitude=-57.718,
            minimum_latitude=82.892,
            maximum_latitude=83.307,
            start_datetime="1993-01-01T00:00:00",
            end_datetime="2021-06-30T23:59:59",
            output_filename=output_file)

# second dataset ID
for var in data_variables:
    output_file = os.path.join(folder_path, f"{var}_id2.nc")
    if os.path.exists(output_file):
        pass
    else:
        copernicusmarine.subset(
            dataset_id="cmems_mod_glo_phy_myint_0.083deg_P1D-m",
            variables=[var],
            minimum_longitude=-58.133,
            maximum_longitude=-57.718,
            minimum_latitude=82.892,
            maximum_latitude=83.307,
            start_datetime="2021-07-01T00:00:00",
            end_datetime="2023-07-31T23:59:59",
            output_filename=os.path.join(folder_path, f"{var}_id2.nc"))

print("down")

os.makedirs(os.path.join(folder_path, "Merged"), exist_ok=True)

for var in data_variables:
    output_file = os.path.join(folder_path, "Merged", f"{var}_merged.nc")
    if os.path.exists(output_file):
        pass
    else:
        data_id1_file = os.path.join(folder_path, f"{var}_id1.nc")
        data_id2_file = os.path.join(folder_path, f"{var}_id2.nc")
        data_id1_xr = xr.open_dataset(data_id1_file)
        data_id2_xr = xr.open_dataset(data_id2_file)
        data_xr = xr.merge([data_id1_xr, data_id2_xr])
        data_file = os.path.join(folder_path, "Merged", f"{var}_merged.nc")
        data_xr.to_netcdf(data_file)

print("down")
#extract training_data
#create variable for time slice
training_data = {}
for var in data_variables:
    data_file = os.path.join(folder_path, "Merged", f"{var}_merged.nc")
    selection_dataset = xr.open_dataset(data_file)
    selection_dataset_time = selection_dataset.sel(time=slice('1993-01-01', '2018-12-31'))

    if 'depth' in selection_dataset_time[var].dims: #drop "depth" if it exists
        selection_dataset_time[var] = selection_dataset_time[var].mean(dim='depth')
        selection_dataset_time = selection_dataset_time.drop_vars("depth")
        check_nans = selection_dataset_time[var].isnull().any()
        if check_nans: #complete data via linear interpolate
            selection_dataset_time[var] = selection_dataset_time[var].interpolate_na(dim='time')
    else:
        check_nans = selection_dataset_time[var].isnull().any()
        if check_nans:
            selection_dataset_time[var] = selection_dataset_time[var].interpolate_na(dim='time')

    training_data[var] = selection_dataset_time

#check if dimensions same: only keep time, lat and lon
dimensions = None
for var, dataset in training_data.items():
    if dimensions is None:
        dimensions = dataset.dims
    elif dimensions != dataset.dims:
        raise ValueError(f"Dimension mismatch in variable {var}")

train = xr.merge([training_data[var] for var in data_variables])

#get input and output variables
x_train_xr = train[["siconc", "thetao", "bottomT", "so", "usi", "vsi", "uo", "vo"]]
y_train_xr = train["sithick"]
cwd = os.getcwd()
model_path = os.path.join(cwd,'saved_model')
model_mse = load_model(os.path.join(model_path,'NN_mse_model.h5'))
model_mae = load_model(os.path.join(model_path,'NN_mae_model.h5'))