import xarray as xr
import os

# Base path
base_path = 'C:\\Users\\12603\\Desktop\\sea ice\\EAEE4000_MLProject\\sea ice thickness dataset\\site selection one-greenland'

# List of variable needed to be combined
var_names = ['bottomT', 'siconc', 'sithick', 'so', 'thetao', 'uo', 'usi', 'vo', 'vsi']

for var in var_names:
    my_file = os.path.join(base_path, f'{var}.nc')
    myint_file = os.path.join(base_path, f'{var}_test.nc')
    ds_my = xr.open_dataset(my_file)
    ds_myint = xr.open_dataset(myint_file)
    ds_merged = xr.merge([ds_my, ds_myint])

    # Save the merged dataset
    merged_file = os.path.join(base_path, f'{var}_merged.nc')
    ds_merged.to_netcdf(merged_file)
print("done")