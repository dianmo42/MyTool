# plot data with linear axes

import matplotlib.pyplot as plt
import numpy as np

# read data
fname = "../bench/linear.dat"
data = np.loadtxt(fname, dtype=float, comments='#')
T = data[:, 0]
E = data[:, 1]
V = data[:, 2]

# plot temperature dependence of energy
fig, ax = plt.subplots(figsize=(3.375, 2.875))

ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Potential Energy (eV)")
ax.set_xlim((0, 2000))
ax.set_ylim((-5, -4.6))
ax.set_xticks(np.arange(0, 2001, 500))
ax.set_yticks(np.arange(-4.95, -4.6, 0.1))

ax.plot(T, E, 'o')
ax.plot(T, E - 0.05, '-')

plt.savefig("../figure/linear.png")