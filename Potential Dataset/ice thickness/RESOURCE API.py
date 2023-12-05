<<<<<<< HEAD
import copernicus_marine_client as copernicusmarine
copernicusmarine.login("xfeng4","ZhaoXiaoBai1")
copernicusmarine.subset(
  dataset_id="cmems_mod_glo_phy_my_0.083_P1D-m",
  variables=["vsi"],
  minimum_longitude=-167.38624489143544,
  maximum_longitude=-167.38624489143544,
  minimum_latitude=76.0326969760851,
  maximum_latitude=76.0326969760851,
  start_datetime="2015-01-01T00:00:00",
  end_datetime="2020-10-16T23:59:59",
  output_filename="vsi.nc",
)
=======
import copernicus_marine_client as copernicusmarine
copernicusmarine.login("xfeng4","ZhaoXiaoBai1")
copernicusmarine.subset(
  dataset_id="cmems_mod_glo_phy_my_0.083_P1D-m",
  variables=["vsi"],
  minimum_longitude=-167.38624489143544,
  maximum_longitude=-167.38624489143544,
  minimum_latitude=76.0326969760851,
  maximum_latitude=76.0326969760851,
  start_datetime="2015-01-01T00:00:00",
  end_datetime="2020-10-16T23:59:59",
  output_filename="vsi.nc",
)
>>>>>>> 9a16eed606395667348c4ef240998140a7db3d56
print("down")