import numpy as np

# read data
fname = "./data-1.dat"
data = np.loadtxt(fname, dtype=float, skiprows=0, comments="#")

nfile = 4
for i in range(1, nfile, 1):
    fname = "./data-%d.dat" % (i + 1)
    data_tmp = np.loadtxt(fname, dtype=float, skiprows=0, comments="#")
    
    data += data_tmp

# write data
fname = "./data-ave.dat"
np.savetxt(fname, data / nfile, fmt="%.3f", newline="\n")