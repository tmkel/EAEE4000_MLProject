<<<<<<< HEAD
import numpy as np
import xarray as xr
import scipy.stats

sithick_ds = xr.open_dataset('C:\\Users\\12603\\Desktop\\sea ice\\sithick.nc')
siconc_ds = xr.open_dataset('C:\\Users\\12603\\Desktop\\sea ice\\siconc.nc')
so_ds = xr.open_dataset('C:\\Users\\12603\\Desktop\\sea ice\\so.nc')
thetao_ds = xr.open_dataset('C:\\Users\\12603\\Desktop\\sea ice\\thetao.nc')
usi_ds = xr.open_dataset('C:\\Users\\12603\\Desktop\\sea ice\\usi.nc')
vsi_ds = xr.open_dataset('C:\\Users\\12603\\Desktop\\sea ice\\vsi.nc')

print(sithick_ds)


# Function to calculate correlation over time
def calculate_correlation(ds1, ds2, var1, var2):
    # Replace NaNs with a fill value, e.g., the mean or median
    fill_value_1 = ds1[var1].mean()
    fill_value_2 = ds2[var2].mean()

    # Fill NaNs
    data1 = ds1[var1].fillna(fill_value_1)
    data2 = ds2[var2].fillna(fill_value_2)

    # Replace Infs with the fill value
    data1 = data1.where(np.isfinite(data1), fill_value_1)
    data2 = data2.where(np.isfinite(data2), fill_value_2)

    # Flatten the data arrays and compute Pearson's correlation coefficient
    return scipy.stats.pearsonr(data1.values.flatten(), data2.values.flatten())[0]

# Calculate correlations
correlations = {
    "sithick_vs_siconc": calculate_correlation(sithick_ds, siconc_ds, 'sithick', 'siconc'),
    #"sithick_vs_so": calculate_correlation(sithick_ds, so_ds, 'sithick', 'so'),
    #"sithick_vs_thetao": calculate_correlation(sithick_ds, thetao_ds, 'sithick', 'thetao'),
    "sithick_vs_usi": calculate_correlation(sithick_ds, usi_ds, 'sithick', 'usi'),
    "sithick_vs_vsi": calculate_correlation(sithick_ds, vsi_ds, 'sithick', 'vsi')
}

for key, value in correlations.items():
    print(f"{key}: {value}")

sithick_ds.close()
siconc_ds.close()
so_ds.close()
thetao_ds.close()
usi_ds.close()
vsi_ds.close()
=======
import numpy as np
import xarray as xr
import scipy.stats

sithick_ds = xr.open_dataset('C:\\Users\\12603\\Desktop\\sea ice\\sithick.nc')
siconc_ds = xr.open_dataset('C:\\Users\\12603\\Desktop\\sea ice\\siconc.nc')
so_ds = xr.open_dataset('C:\\Users\\12603\\Desktop\\sea ice\\so.nc')
thetao_ds = xr.open_dataset('C:\\Users\\12603\\Desktop\\sea ice\\thetao.nc')
usi_ds = xr.open_dataset('C:\\Users\\12603\\Desktop\\sea ice\\usi.nc')
vsi_ds = xr.open_dataset('C:\\Users\\12603\\Desktop\\sea ice\\vsi.nc')

print(sithick_ds)


# Function to calculate correlation over time
def calculate_correlation(ds1, ds2, var1, var2):
    # Replace NaNs with a fill value, e.g., the mean or median
    fill_value_1 = ds1[var1].mean()
    fill_value_2 = ds2[var2].mean()

    # Fill NaNs
    data1 = ds1[var1].fillna(fill_value_1)
    data2 = ds2[var2].fillna(fill_value_2)

    # Replace Infs with the fill value
    data1 = data1.where(np.isfinite(data1), fill_value_1)
    data2 = data2.where(np.isfinite(data2), fill_value_2)

    # Flatten the data arrays and compute Pearson's correlation coefficient
    return scipy.stats.pearsonr(data1.values.flatten(), data2.values.flatten())[0]

# Calculate correlations
correlations = {
    "sithick_vs_siconc": calculate_correlation(sithick_ds, siconc_ds, 'sithick', 'siconc'),
    #"sithick_vs_so": calculate_correlation(sithick_ds, so_ds, 'sithick', 'so'),
    #"sithick_vs_thetao": calculate_correlation(sithick_ds, thetao_ds, 'sithick', 'thetao'),
    "sithick_vs_usi": calculate_correlation(sithick_ds, usi_ds, 'sithick', 'usi'),
    "sithick_vs_vsi": calculate_correlation(sithick_ds, vsi_ds, 'sithick', 'vsi')
}

for key, value in correlations.items():
    print(f"{key}: {value}")

sithick_ds.close()
siconc_ds.close()
so_ds.close()
thetao_ds.close()
usi_ds.close()
vsi_ds.close()
>>>>>>> 9a16eed606395667348c4ef240998140a7db3d56
