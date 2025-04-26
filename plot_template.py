## This script generates a plot using matplotlib with specific formatting and styles.
## Required libraries: numpy, matplotlib

import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

## Import data
data = np.loadtxt('template.dat', comments='#')
X = data[:, 0]
Y = data[:, 1]

## Figure size
fig_width = 3.385                   # inches
fig_height = fig_width * 0.75       # aspect ratio
plt.rcParams.update({
    "font.family": "Times New Roman",
    "text.usetex": True,
    "font.size": 8,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "figure.figsize": (fig_width, fig_height),
    "lines.markersize": 3,
    "axes.linewidth": 1,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.major.size": 3,
    "ytick.major.size": 3,
})

fig, ax = plt.subplots()

## Axis limits and scales
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
plt.xscale('linear')
plt.yscale('linear')
# plt.xscale('log')
# plt.yscale('log')
ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=5))  # for x-axis
ax.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=5))  # for y-axis

## Labels and ticks
ax.set_xlabel(r'$T\,(\mathrm{K})$')
ax.set_ylabel(r'$E_\mathrm{pot}\,(\mathrm{eV})$')
ax.tick_params(which='both', top=True, right=True)

# Colormap
cmap = cm.rainbow

### Scatter and line
ax.scatter(X, Y, color='black', s=30, marker='o', facecolors='white', edgecolors='black', linewidth=0.75)
ax.plot(X, Y, color=cmap(0.2), linewidth=1.5, zorder = 2)


plt.savefig("template.png", dpi=600, bbox_inches='tight')
# plt.show()
