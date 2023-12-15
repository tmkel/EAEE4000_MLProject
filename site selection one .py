import copernicus_marine_client as copernicusmarine
copernicusmarine.login("xfeng4","ZhaoXiaoBai1")
# train
# DATASET VARIABLE "sithick","siconc","thetao","bottomT","so", "usi", "vsi","uo","vo"
for var in ["uo","vo"]:
    copernicusmarine.subset(
      dataset_id="cmems_mod_glo_phy_my_0.083deg_P1D-m",
      variables=[var],
      minimum_longitude=-58.133,
      maximum_longitude=-57.718,
      minimum_latitude=82.892,
      maximum_latitude=83.307,
      start_datetime="1993-01-01T00:00:00",
      end_datetime="2021-06-30T23:59:59",
      output_filename=f"{var}.nc",
  )

# test
for var in ["uo","vo"]:
    copernicusmarine.subset(
      dataset_id="cmems_mod_glo_phy_myint_0.083deg_P1D-m",
      variables=[var],
      minimum_longitude=-58.133,
      maximum_longitude=-57.718,
      minimum_latitude=82.892,
      maximum_latitude=83.307,
      start_datetime="2021-07-01T00:00:00",
      end_datetime="2023-07-31T23:59:59",
      output_filename=f"{var}_test.nc",
    )
print("down")