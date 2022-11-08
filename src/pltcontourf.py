# plot contourf
# input: RRTM simulation

import math
import numpy as np
import matplotlib.pyplot as plt
import h5py

path1 = '../dat/'
filename1 = 'rrtm_simulation_all_lat.h5'

with h5py.File(path1+filename1, 'r') as data:
    for group in data.keys() :
        print (group)

# adding [()]
# because When we assign f['default'] to the variable data.
# We are not reading the data from the file.
# Instead, we are generating a pointer to where the data is located on the hard drive.
    ds_data = data['.']['heating_rate(K_day-1)'][()]
#    print (ds_data.shape, ds_data.dtype)
    ds_data1 = data['.']['pressure(mb)'][()]
#    print (ds_data1.shape, ds_data1.dtype)
    ds_data2 = data['.']['date'][()]
#    print (ds_data2.shape, ds_data2.dtype)
    ds_data3 = data['.']['latitude_dim'][()]
#    print (ds_data3.shape, ds_data3.dtype)

arr_r = ds_data[445,:,19:44]
ds_Y = ds_data3[:]
ds_X = ds_data1[:]
#print(ds_X)
ds_X = np.log(1000./ds_data1[:]) * 7.
#print(ds_X)
ds_X = ds_X[19:44]
#print(ds_X)

fig, ax = plt.subplots(figsize=(7, 10))

levels = np.arange(-5, 0.5, 0.3)
CS = ax.contourf(ds_X, ds_Y, arr_r, levels, origin='lower', cmap='nipy_spectral', extend='both',
                linewidths=2)#, extent=(1, 200, -80, 80))
ax.clabel(CS, inline=True, fontsize=10)

#ax.set_yticks([0,3,6,9,12,15])
#ax.set_yticklabels(labels=[33,30,27,24,21,18])
ax.set_xlabel('Altitude (km)', fontsize=16)
ax.set_ylabel('Latitude (deg)', fontsize=16, rotation=270)
#ax.set_xticks([0,19,39,59,79,99,119,139,159])
#ax.set_xticklabels(labels=['1','20','40','60','80','100','120','140','160'])

#ax.set_xlim(1,200)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

CBI = fig.colorbar(CS, orientation='horizontal', shrink=0.8)

# Create colorbar
#cbar = ax.figure.colorbar(im, ax=ax, ticks=[0.01,0.05,0.10,0.15,0.2,0.25,0.3], orientation="horizontal", fraction=0.050)
#cbar.ax.set_xlabel('particle size ('+'$\mu$'+'m)', fontsize=16)
##cbar.ax.set_ylabel('heating rate', rotation=-90, va="bottom")
#cbar.ax.tick_params(labelsize=14)

pngname = "../fig/"+"test_all_lat.png"
print("save ", pngname)
plt.savefig(pngname, bbox_inches='tight')


