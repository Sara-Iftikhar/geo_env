import os
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
from netCDF4 import Dataset

# %%
dset = Dataset(r'E:\AA\HYXE_consultancy\geo_env\Climate_Model_Data\tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_195001-201412.nc')
print(dset.variables)

# %%
# Question 05 (Which variables does the netCDF contain?)
# It contains nine variables which are listed below

print(dset.variables.keys())

# %%
# Question 06 (What are the dimensions of the air temperature variable?)

print(dset.variables['tas'])

# It has a dimension of (780, 180, 288) which represents (time, lat, lon)

print(dset.variables['tas'].shape)

# %%
# Question 08 (What is the data type of the air temperature variables: integer, single, or double?)
# data type of the air temperature variable is `Float32`

print(dset.variables['tas'].dtype)

# %%
# Question 16 (What type of model does the data originate from: physically-based, conceptual, data-driven, or hybrid?)
# Since the experiment attribute is 'all-forcing simulation of the recent past,' and the experiment_id is 'historical',
# so its more likely a physically-based model.

print(dset.experiment)
print(dset.experiment_id)

dset.close()

# %%
# Question 17 (Calculate the mean air temperature map for 1850–1900 (also known as the pre-industrial period).)

fpath = r'E:\AA\HYXE_consultancy\geo_env\Climate_Model_Data\tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_185001-194912.nc'
dset_1850 = xr.open_dataset(fpath)
tas_maps = dset_1850['tas'].sel(time=slice('18500116', '19001231')).mean(axis=0)
print(tas_maps)

# %%

# Question 18 (Calculate mean air temperature maps for 2071–2100 for each climate scenario using the np.mean function)

# defining paths to the dataset for each scenario
fp_ssp119 = r'E:\AA\HYXE_consultancy\geo_env\Climate_Model_Data\tas_Amon_GFDL-ESM4_ssp119_r1i1p1f1_gr1_201501-210012.nc'
fp_ssp245 = r'E:\AA\HYXE_consultancy\geo_env\Climate_Model_Data\tas_Amon_GFDL-ESM4_ssp245_r1i1p1f1_gr1_201501-210012.nc'
fp_ssp585 = r'E:\AA\HYXE_consultancy\geo_env\Climate_Model_Data\tas_Amon_GFDL-ESM4_ssp585_r1i1p1f1_gr1_201501-210012.nc'

# opening dataset for each scenario
dset_ssp119 = xr.open_dataset(fp_ssp119)
dset_ssp245 = xr.open_dataset(fp_ssp245)
dset_ssp585 = xr.open_dataset(fp_ssp585)

# the mean air temperature map for SSP119 scenario is given below
mean_tas_ssp119 = np.mean(dset_ssp119['tas'].sel(time=slice('20710101', '21001231')), axis=0)
# the mean air temperature map for SSP245 scenario is given below
mean_tas_ssp245 = np.mean(dset_ssp245['tas'].sel(time=slice('20710101', '21001231')), axis=0)
# the mean air temperature map for SSP585 scenario is given below
mean_tas_ssp585 = np.mean(dset_ssp585['tas'].sel(time=slice('20710101', '21001231')), axis=0)

print(f'the mean air temperature map for SSP119 scenario is: {mean_tas_ssp119}')
print(f'the mean air temperature map for SSP245 scenario is: {mean_tas_ssp245}')
print(f'the mean air temperature map for SSP585 scenario is: {mean_tas_ssp585}')

# %%

path = os.path.join(os.getcwd(), 'figures')
if not os.path.exists(path):
      os.mkdir(path)

# %%

# Question 19
# (Compute and visualize the temperature differences between 2071–2100 and 1850–1900 for each scenario.
# Use libraries like matplotlib for creating the visualizations. Ensure your visualizations are of high quality and saved as PNG using,
# for example, plt.savefig(’filename.png’, dpi=300). Ensure your plots include clear legends, color bars, titles, and axis labels)

dset_1850['tas'].sel(time=slice('18500116', '19001231')).mean(axis=0).plot()
ax = plt.gca()
ax.set_title('Mean Average Temperature Map from 1850 to 1900')
plt.savefig(os.path.join(path, 'mean_tas_1850_1900'), dpi=300)
plt.show()

dset_ssp119['tas'].sel(time=slice('20710101', '21001231')).mean(axis=0).plot()
ax = plt.gca()
ax.set_title('Mean Average Temperature Map from 2071 to 2100 for ssp119')
plt.savefig(os.path.join(path, 'mean_tas_2071_2100_ssp119'), dpi=300)
plt.show()

dset_ssp245['tas'].sel(time=slice('20710101', '21001231')).mean(axis=0).plot()
ax = plt.gca()
ax.set_title('Mean Average Temperature Map from 2071 to 2100 for ssp245')
plt.savefig(os.path.join(path, 'mean_tas_2071_2100_ssp245'), dpi=300)
plt.show()

dset_ssp585['tas'].sel(time=slice('20710101', '21001231')).mean(axis=0).plot()
ax = plt.gca()
ax.set_title('Mean Average Temperature Map from 2071 to 2100 for ssp585')
plt.savefig(os.path.join(path, 'mean_tas_2071_2100_ssp585'), dpi=300)
plt.show()


# Exercise 04

# Question 01 (To analyze climate data for your city, find its latitude and longitude, then convert these to x,y
# indices based on the climate model’s grid system.)
# Latitude and Longitude of my city `Islamabad` are 33.738045 and 73.084488 respectively.

islamabad_lat = 33.738045
islamabad_lon = 73.084488

# Find nearest grid points in the model dataset for 1850
nearest_lat_index = abs(dset_1850['lat'] - islamabad_lat).argmin().item()
nearest_lon_index = abs(dset_1850['lon'] - islamabad_lon).argmin().item()

# Question 02 (Extract the air temperature time series data for your city from the five netCDF files.)

# Extract data at Islamabad's location
climate_data_at_islamabad_1850 = dset_1850['tas'].isel(lat=nearest_lat_index, lon=nearest_lon_index)

# %%

fp_1950 = r'E:\AA\HYXE_consultancy\geo_env\Climate_Model_Data\tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_195001-201412.nc'

dset_1950 = xr.open_dataset(fp_1950)

nearest_lat_index = abs(dset_1950['lat'] - islamabad_lat).argmin().item()
nearest_lon_index = abs(dset_1950['lon'] - islamabad_lon).argmin().item()

climate_data_at_islamabad_1950 = dset_1950['tas'].isel(lat=nearest_lat_index, lon=nearest_lon_index)

# %%

nearest_lat_index = abs(dset_ssp119['lat'] - islamabad_lat).argmin().item()
nearest_lon_index = abs(dset_ssp119['lon'] - islamabad_lon).argmin().item()

climate_data_at_islamabad_ssp119 = dset_ssp119['tas'].isel(lat=nearest_lat_index, lon=nearest_lon_index)

# %%

nearest_lat_index = abs(dset_ssp245['lat'] - islamabad_lat).argmin().item()
nearest_lon_index = abs(dset_ssp245['lon'] - islamabad_lon).argmin().item()

climate_data_at_islamabad_ssp245 = dset_ssp245['tas'].isel(lat=nearest_lat_index, lon=nearest_lon_index)

# %%

nearest_lat_index = abs(dset_ssp585['lat'] - islamabad_lat).argmin().item()
nearest_lon_index = abs(dset_ssp585['lon'] - islamabad_lon).argmin().item()

climate_data_at_islamabad_ssp585 = dset_ssp585['tas'].isel(lat=nearest_lat_index, lon=nearest_lon_index)

# Question 03 (What is the mean air temperature change projected for your city in the 2071–2100 period
# compared to the pre-industrial period (1850–1900) for each scenario?)

isl_1850 = climate_data_at_islamabad_1850.sel(time=slice('18500116', '19001231')).mean(axis=0).data.item()
isl_ssp119 = climate_data_at_islamabad_ssp119.sel(time=slice('20710101', '21001231')).mean(axis=0).data.item()
isl_ssp245 = climate_data_at_islamabad_ssp245.sel(time=slice('20710101', '21001231')).mean(axis=0).data.item()
isl_ssp585 = climate_data_at_islamabad_ssp585.sel(time=slice('20710101', '21001231')).mean(axis=0).data.item()

print(f'Mean air temperature change projected for Islamabad in the (2071–2100) period compared to the '
      f'pre-industrial period (1850–1900) for SSP119 is {isl_ssp119-isl_1850}')

# %%

print(f'Mean air temperature change projected for Islamabad in the (2071–2100) period compared to the '
      f'pre-industrial period (1850–1900) for SSP245 is {isl_ssp245-isl_1850}')

# %%

print(f'Mean air temperature change projected for Islamabad in the (2071–2100) period compared to the '
      f'pre-industrial period (1850–1900) for SSP585 is {isl_ssp585-isl_1850}')

# Question 04 (What is the global average projected temperature change for each scenario?)

global_1850 = dset_1850['tas'].sel(time=slice('18500116', '19001231')).mean().data.item()
global_ssp119 = dset_ssp119['tas'].sel(time=slice('20710101', '21001231')).mean().data.item()
global_ssp245 = dset_ssp245['tas'].sel(time=slice('20710101', '21001231')).mean().data.item()
global_ssp585 = dset_ssp585['tas'].sel(time=slice('20710101', '21001231')).mean().data.item()

print(f'global average projected temperature change in the (2071–2100) period compared to the '
      f'pre-industrial period (1850–1900) for SSP119 is {global_ssp119-global_1850}')

# %%

print(f'global average projected temperature change in the (2071–2100) period compared to the '
      f'pre-industrial period (1850–1900) for SSP245 is {global_ssp245-global_1850}')

# %%

print(f'global average projected temperature change in the (2071–2100) period compared to the '
      f'pre-industrial period (1850–1900) for SSP585 is {global_ssp585-global_1850}')

# Question 05 (Create air temperature time series plots for 1850–2100. Ensure your plots include clear
# legends, color bars, titles, and axis labels. Export your figures as high-quality PNG files.)

combined_dset_ssp119 = xr.concat([dset_1850, dset_1950, dset_ssp119], dim='time')

combined_dset_ssp119['tas'].sel(time=slice('18500116', '21001216')).mean(axis=(1,2)).plot()
ax = plt.gca()
ax.set_title('Air Temperature time series plot for 1850–2100 for SSP119')
plt.savefig(os.path.join(path, 'air_temp_time_series_1850-2100_ssp119'), dpi=300)
plt.show()

# %%

combined_dset_ssp245 = xr.concat([dset_1850, dset_1950, dset_ssp245], dim='time')

combined_dset_ssp245['tas'].sel(time=slice('18500116', '21001216')).mean(axis=(1,2)).plot()
ax = plt.gca()
ax.set_title('Air Temperature time series plot for 1850–2100 for SSP245')
plt.savefig(os.path.join(path, 'air_temp_time_series_1850-2100_ssp245'), dpi=300)
plt.show()

# %%

combined_dset_ssp585 = xr.concat([dset_1850, dset_1950, dset_ssp585], dim='time')

combined_dset_ssp585['tas'].sel(time=slice('18500116', '21001216')).mean(axis=(1,2)).plot()
ax = plt.gca()
ax.set_title('Air Temperature time series plot for 1850–2100 for SSP585')
plt.savefig(os.path.join(path, 'air_temp_time_series_1850-2100_ssp585'), dpi=300)
plt.show()

# Question 08 (Bonus Challenge: Create plots that compare both the global averages and the temperature
# changes specific to your city.)

# Find nearest grid points in the model dataset for SSP119
nearest_lat_index = abs(combined_dset_ssp119['lat'] - islamabad_lat).argmin().item()
nearest_lon_index = abs(combined_dset_ssp119['lon'] - islamabad_lon).argmin().item()

# Extract data at Islamabad's location
combined_isl_ssp119 = combined_dset_ssp119['tas'].isel(lat=nearest_lat_index, lon=nearest_lon_index)

# %%

# Find nearest grid points in the model dataset for SSP245
nearest_lat_index = abs(combined_dset_ssp245['lat'] - islamabad_lat).argmin().item()
nearest_lon_index = abs(combined_dset_ssp245['lon'] - islamabad_lon).argmin().item()

# Extract data at Islamabad's location
combined_isl_ssp245 = combined_dset_ssp245['tas'].isel(lat=nearest_lat_index, lon=nearest_lon_index)

# %%

# Find nearest grid points in the model dataset for SSP585
nearest_lat_index = abs(combined_dset_ssp585['lat'] - islamabad_lat).argmin().item()
nearest_lon_index = abs(combined_dset_ssp585['lon'] - islamabad_lon).argmin().item()

# Extract data at Islamabad's location
combined_isl_ssp585 = combined_dset_ssp585['tas'].isel(lat=nearest_lat_index, lon=nearest_lon_index)

# %%

combined_dset_ssp119['tas'].sel(time=slice('18500116', '21001216')).mean(axis=(1,2)).plot(alpha=0.4, label='Combined global SSP119')
combined_isl_ssp119.plot(alpha=0.4, label='Combined Islamabad SSP119')
plt.legend()
ax = plt.gca()
ax.set_title('Comparison of global averages and the temperature changes specific to Islamabad for SSP119')
plt.savefig(os.path.join(path, 'air_temp_time_series_comparison_ssp119'), dpi=300)
plt.show()

# %%

combined_dset_ssp245['tas'].sel(time=slice('18500116', '21001216')).mean(axis=(1,2)).plot(alpha=0.4, label='Combined global SSP245')
combined_isl_ssp245.plot(alpha=0.4, label='Combined Islamabad SSP245')
plt.legend()
ax = plt.gca()
ax.set_title('Comparison of global averages and the temperature changes specific to Islamabad for SSP245')
plt.savefig(os.path.join(path, 'air_temp_time_series_comparison_ssp245'), dpi=300)
plt.show()

# %%

combined_dset_ssp585['tas'].sel(time=slice('18500116', '21001216')).mean(axis=(1,2)).plot(alpha=0.4, label='Combined global SSP585')
combined_isl_ssp585.plot(alpha=0.4, label='Combined Islamabad SSP585')
plt.legend()
ax = plt.gca()
ax.set_title('Comparison of global averages and the temperature changes specific to Islamabad for SSP585')
plt.savefig(os.path.join(path, 'air_temp_time_series_comparison_ssp585'), dpi=300)
plt.show()