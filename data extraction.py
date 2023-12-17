"""
data extraction.py
1.
"""

import xarray as xr
import os
import matplotlib.pyplot as plt

#vsi loss data !!!!, lose a large portion of data, 
#
#cwd
train_path = 'C:\\Users\\12603\\Desktop\\sea ice\\EAEE4000_MLProject\\sea ice thickness dataset\\site selection one-greenland'
test_path = 'C:\\Users\\12603\\Desktop\\sea ice\\EAEE4000_MLProject\\sea ice thickness dataset\\site selection one-greenland'

# all files name
files_name = [
    'bottomT_merged.nc',
    'siconc_merged.nc',
    'sithick_merged.nc',
    'so_merged.nc',
    'vo_merged.nc',
    'vsi_merged.nc',
    'uo_merged.nc',
    'thetao_merged.nc',
    'usi_merged.nc']

# extract training_data
training_data = {}
for var in files_name:
    file_path = os.path.join(train_path, var)
    selection_dataset = xr.open_dataset(file_path)
    selection_dataset_time = selection_dataset.sel(time=slice('1993-01-01', '2018-12-31'))

    for data_var in selection_dataset_time.data_vars:
        if 'depth' in selection_dataset_time[data_var].dims:
            # average over the 'depth' dimension
            selection_dataset_time[data_var] = selection_dataset_time[data_var].mean(dim='depth')
            check_nans = selection_dataset_time[data_var].isnull().any()
            if check_nans:
                # # forward and backward method
                # selection_dataset_time[data_var] = selection_dataset_time[data_var].ffill(dim='time').ffill(dim='latitude').ffill(dim='longitude')
                # selection_dataset_time[data_var] = selection_dataset_time[data_var].ffill(dim='time').ffill(dim='latitude').ffill(dim='longitude')
                # # lon and lat method
                # selection_dataset_time[data_var] = selection_dataset_time[data_var].interpolate_na(dim='latitude', method='nearest')
                # selection_dataset_time[data_var] = selection_dataset_time[data_var].interpolate_na(dim='longitude', method='nearest')
                # # time method
                selection_dataset_time[data_var] = selection_dataset_time[data_var].interpolate_na(dim='time')

        else:
            # 'depth' is not a dimension
            check_nans = selection_dataset_time[data_var].isnull().any()
            if check_nans:
                # # forward and backward method
                # selection_dataset_time[data_var] = selection_dataset_time[data_var].ffill(dim='time').ffill(
                #     dim='latitude').ffill(dim='longitude')
                # selection_dataset_time[data_var] = selection_dataset_time[data_var].ffill(dim='time').ffill(
                #     dim='latitude').ffill(dim='longitude')
                # # lon and lat method
                # selection_dataset_time[data_var] = selection_dataset_time[data_var].interpolate_na(dim='latitude',
                #                                                                                    method='nearest')
                # selection_dataset_time[data_var] = selection_dataset_time[data_var].interpolate_na(dim='longitude',
                #                                                                                    method='nearest')
                # time method
                selection_dataset_time[data_var] = selection_dataset_time[data_var].interpolate_na(dim='time')
        training_data[var] = selection_dataset_time

# extract testing_data
testing_data = {}

for var in files_name:
    file_path = os.path.join(train_path, var)
    selection_dataset = xr.open_dataset(file_path)
    selection_dataset_time = selection_dataset.sel(time=slice('2019-01-01', '2023-07-31'))

    for data_var in selection_dataset_time.data_vars:
        if 'depth' in selection_dataset_time[data_var].dims:
            # average over the 'depth' dimension
            selection_dataset_time[data_var] = selection_dataset_time[data_var].mean(dim='depth')
            check_nans = selection_dataset_time[data_var].isnull().any()
            if check_nans:
                # # forward and backward method
                # selection_dataset_time[data_var] = selection_dataset_time[data_var].ffill(dim='time').ffill(
                #     dim='latitude').ffill(dim='longitude')
                # selection_dataset_time[data_var] = selection_dataset_time[data_var].ffill(dim='time').ffill(
                #     dim='latitude').ffill(dim='longitude')
                # # lon and lat method
                # selection_dataset_time[data_var] = selection_dataset_time[data_var].interpolate_na(dim='latitude',
                #                                                                                    method='nearest')
                # selection_dataset_time[data_var] = selection_dataset_time[data_var].interpolate_na(dim='longitude',
                #                                                                                    method='nearest')
                # time method
                selection_dataset_time[data_var] = selection_dataset_time[data_var].interpolate_na(dim='time')
        else:
            # 'depth' is not a dimension
            check_nans = selection_dataset_time[data_var].isnull().any()
            if check_nans:
                # # forward and backward method
                # selection_dataset_time[data_var] = selection_dataset_time[data_var].ffill(dim='time').ffill(
                #     dim='latitude').ffill(dim='longitude')
                # selection_dataset_time[data_var] = selection_dataset_time[data_var].ffill(dim='time').ffill(
                #     dim='latitude').ffill(dim='longitude')
                # # lon and lat method
                # selection_dataset_time[data_var] = selection_dataset_time[data_var].interpolate_na(dim='latitude',
                #                                                                                    method='nearest')
                # selection_dataset_time[data_var] = selection_dataset_time[data_var].interpolate_na(dim='longitude',
                #                                                                                    method='nearest')
                # # time method
                selection_dataset_time[data_var] = selection_dataset_time[data_var].interpolate_na(dim='time')
        testing_data[var] = selection_dataset_time

#built training dataset
bottomT_train = training_data['bottomT_merged.nc']
siconc_train = training_data['siconc_merged.nc']
so_train = training_data['so_merged.nc']
vo_train = training_data['vo_merged.nc']
vsi_train = training_data['vsi_merged.nc']
uo_train = training_data['uo_merged.nc']
thetao_train = training_data['thetao_merged.nc']
usi_train = training_data['usi_merged.nc']
sithick_train = training_data['sithick_merged.nc']

#built testing dataset
bottomT_test = testing_data['bottomT_merged.nc']
siconc_test = testing_data['siconc_merged.nc']
so_test = testing_data['so_merged.nc']
vo_test = testing_data['vo_merged.nc']
vsi_test = testing_data['vsi_merged.nc']
uo_test = testing_data['uo_merged.nc']
thetao_test = testing_data['thetao_merged.nc']
usi_test = testing_data['usi_merged.nc']
sithick_test = testing_data['sithick_merged.nc']

# example 1, input: 1993 -2018, output:1993 -2018
x_train_dataset1 = xr.merge([bottomT_train, siconc_train, so_train, vo_train, vsi_train, uo_train, thetao_train, usi_train])
y_train_dataset1 = sithick_train

# example 2 input: 1993 -2018, output:2019-2023
x_train_dataset1 = xr.merge([bottomT_train, siconc_train, so_train, vo_train, vsi_train, uo_train, thetao_train, usi_train])
y_train_dataset1 = sithick_test

# # Access the specific dataset from the dictionary
# selected_dataset = testing_data['vsi_merged.nc']
# selected_data_at_first_time_step = selected_dataset.isel(time=0,latitude=0,longitude=0)
# print(selected_data_at_first_time_step)
#
#
# # Check NaN values in each variable of each dataset
# for file_name, dat in testing_data.items():
#     print(f"NaN values in {file_name}:")
#     for var in dat.data_vars:
#         nan_count = dat[var].isnull().sum().item()  # item() to get a pure Python scalar
#         print(f"  {var}: {nan_count} NaN values")
#
# # # plot test
# file_to_plot = 'vsi_merged.nc'
# var_to_plot = 'vsi'
#
# select_file = testing_data[file_to_plot]
# variable_data = select_file[var_to_plot]
#
# #change time based on needs
# if 'time' in variable_data.dims:
#     variable_data = variable_data.isel(time=0)
#
# variable_data.plot(x='longitude', y='latitude',cmap="Blues_r")
# plt.title(f"{var_to_plot} from {file_to_plot}")
# plt.show()