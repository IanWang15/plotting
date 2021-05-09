"""
used for plotting geospatial figures with scatter

xarray -> dataarray -> numpy array -> cartopy

05/09/2021 v1.0, Yi Wang

"""

import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs

fstd = "../dat/clavrx_MYD021KM.A2019099.1525.modis.level2.nc"

with xr.open_dataset(fstd) as dsstd:
    print(fstd+' is loaded')
    varstd = dsstd['cld_temp_acha']
    lat = dsstd['latitude']
    lon = dsstd['longitude']

fig = plt.figure(figsize=(6, 6))

data = varstd.values
lon = lon.values
lat = lat.values

ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([-60, 0, -50, -10], crs=ccrs.PlateCarree())

mm = ax.scatter(lon.flatten()[::100], lat.flatten()[::100], c=data.flatten()[::100],cmap='rainbow',s=1.2)
ax.coastlines()
ax.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)
#ax.set_title('Cloud Top Temperature (K)')

cbar_ax = fig.add_axes([0.98, 0.25, 0.03, 0.5])
#cbar_ax.set_label('Cloud Top Temperature (K)')

plt.colorbar(mm, cax=cbar_ax)
#ax.set_global()
pngname = "../fig/"+"fig_glob1"+".pdf"
print("save ", pngname)

fig.tight_layout()

pngname = "../fig/"+"fig_cthdiff285"+".pdf"
print("save ", pngname)
plt.savefig(pngname, dpi=100, facecolor='w', edgecolor='w',
    orientation='portrait', papertype=None, format=None,
    transparent=False, bbox_inches='tight', pad_inches=0.1)

plt.show()
