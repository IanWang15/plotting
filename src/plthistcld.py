import matplotlib as mpl
mpl.use('Agg')
import numpy as np
#import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
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

arrcld = np.loadtxt(datdir+'cldType.txt')
arr0 = np.loadtxt(datdir+'cttdiff.txt')

#fig = plt.figure(figsize=(6, 6))

#print(np.shape(dsmodis500.values),np.shape(dslon.values))
#lon = lon[(idxcf == 3.) & (idxmds < 100.)][::100]
#lat = lat[(idxcf == 3.) & (idxmds < 100.)][::100]
#data = data[(idxcf == 3.) & (idxmds < 100.)][::100]

cld = arrcld[::1000]
data = arr0[::1000]
#del arr0

data[data > 25.] = 25.
data[data < -15.] = -15.

#print(np.shape(cld),np.shape(data))

xbins = [-0.5,0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5,13.5]
ybins = np.linspace(-15,25,15)

fig, ax = plt.subplots(figsize=(6, 6))
im = ax.hist2d(cld,data, bins=[xbins,ybins], range=None, density=True, weights=None, cmin=None, cmax=None, norm=LogNorm())
ax.set_xlabel('Cloud Type', fontsize=14)
ax.set_ylabel('CTT difference (K)', fontsize=14)
ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13])
ax.set_yticks([-15,-10,-5,0,5,10,15,20,25])
#plt.colorbar(mm, cax=cbar_ax)

print('start saving')

pngname = "../fig/"+"fig_hist_cldcttdiff_thin_"+filename+".pdf"
print("save ", pngname)
plt.savefig(pngname, bbox_inches='tight')
plt.show()
