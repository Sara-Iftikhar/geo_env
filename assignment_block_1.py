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