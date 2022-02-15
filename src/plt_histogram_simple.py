import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

Y = [0,1,2,3,4,5,6,1,3,5]

print(format(Counter(Y)))

fig, ax = plt.subplots(figsize=(3, 3))
im = ax.hist(Y,bins=[-.5,.5,1.5,2.5,3.5,4.5,5.5],edgecolor="k")
plt.xticks([0,1,2,3,4,5],labels = ['label 1', 'label 2', 'label 3', 'label 4','label 5','label 6'], rotation='vertical')
ax.set_ylabel('number')
pngname = "./"+"fig_hist_simple.pdf"
plt.savefig(pngname, bbox_inches='tight')
