# plot data with logarithmic axes

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# read data
fname1 = "../bench/logarithmic_1.dat"
data1 = np.loadtxt(fname1, dtype=float, comments='#')
x1 = data1[:, 0]
y1 = data1[:, 1]

fname2 = "../bench/logarithmic_2.dat"
data2 = np.loadtxt(fname2, dtype=float, comments='#')
x2 = data2[:, 0]
y2 = data2[:, 1]


# plot self-intermediate scattering function
fig, ax = plt.subplots()
ax.set_xlabel("t (ps)")
ax.set_ylabel("SISF")
ax.set_ylim((0, 1.1))
ax.set_xlim((1E-2, 1E3))
ax.set_xscale("log")
ax.xaxis.set_major_locator(ticker.LogLocator(base=10))
ax.set_yticks(np.arange(0, 1.1, 0.25))
ax.plot(x1, y1, 'b-')
plt.savefig("../figure/logarithmic_1.png")

# plot mean-squared displacement
fig, ax = plt.subplots()
ax.set_xlabel("t (ps)")
ax.set_ylabel("MSD")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim((1E-2, 1E3))
ax.set_ylim((2E-3, 20))
ax.xaxis.set_major_locator(ticker.LogLocator(base=10))
ax.yaxis.set_major_locator(ticker.LogLocator(base=10))
ax.plot(x2, y2, 'r-')
plt.savefig("../figure/logarithmic_2.png")
