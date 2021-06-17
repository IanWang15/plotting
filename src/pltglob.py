import matplotlib as mpl
mpl.use('Agg')
import numpy as np
#import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
#ds_disk = xr.open_dataset("saved_on_disk.nc")
import glob

outputdir1 = '/mnt/efs_clavrx/ywang/run/06082021/dat/pltdat/geospl/day/thin/'
outputdir2 = '/mnt/efs_clavrx/ywang/run/06082021/dat/pltdat/geospl/night/thin/'
outputdir3 = '/mnt/efs_clavrx/ywang/run/06082021/dat/pltdat/geospl8b/day/thin/'
outputdir4 = '/mnt/efs_clavrx/ywang/run/06082021/dat/pltdat/geospl8b/night/thin/'

filename1 = 'day_rrocinoise'
filename2 = 'night_rrocinoise'
filename3 = 'day_rroci8b'
filename4 = 'night_rroci8b'

datdir = outputdir4
filename = filename4

arrlon = np.loadtxt(datdir+'lon.txt')
arrlat = np.loadtxt(datdir+'lat.txt')
arr0 = np.loadtxt(datdir+'cttdiff.txt')

fig = plt.figure(figsize=(6, 6))

#print(np.shape(dsmodis500.values),np.shape(dslon.values))
#lon = lon[(idxcf == 3.) & (idxmds < 100.)][::100]
#lat = lat[(idxcf == 3.) & (idxmds < 100.)][::100]
#data = data[(idxcf == 3.) & (idxmds < 100.)][::100]

lon = arrlon[::2000]
#del arrlon
lat = arrlat[::2000]
#del arrlat
data = arr0[::2000]
#del arr0

print(np.shape(arrlon),np.shape(arrlat),np.shape(arr0))

data[data > 10.] = 10.
data[data < -10.] = -10.

print(np.shape(lon),np.shape(lat),np.shape(data))

ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([-60, 0, -50, -10], crs=ccrs.PlateCarree())

mm = ax.scatter(lon, lat, c=data, alpha = 0.5, cmap='rainbow',s=0.7)
ax.coastlines()
ax.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)
ax.set_title('CTT difference (K); Night; Thin; RROCInoise - MODIS8bands')

cbar_ax = fig.add_axes([0.98, 0.25, 0.03, 0.5])
#cbar_ax.set_label('Cloud Top Temperature (K)')

plt.colorbar(mm, cax=cbar_ax)

ax.set_global()

print('start saving')

pngname = "../fig/"+"fig_glob_cttdiff_thin_"+filename+".pdf"
print("save ", pngname)
plt.savefig(pngname, bbox_inches='tight')
plt.show()
