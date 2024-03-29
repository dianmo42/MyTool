# Python scripts for making plots

### 1. Install `matplotlib` and `numpy`

### 2. Copy `matplotlibrc` to one of the following locations
    
Unix/Linux:

`$HOME/.config/matplotlib/matplotlibrc` or `$XDG_CONFIG_HOME/matplotlib/matplotlibrc` 
(if `$XDG_CONFIG_HOME` is set)

Other platforms:

`$HOME/.matplotlib/matplotlibrc`

These preset parameters make graphs suitable for scientific manuscripts. See [this link](https://matplotlib.org/stable/users/explain/customizing.html#customizing-with-matplotlibrc-files)
for more details.

### 3. Plot data with different python scripts

Data are stored under directory `./bench`.

To plot data with linear axes:
    
    cd src
    python linear.py

This will generate the `linear.png` under `./figure`:

![linear.png](./figure/linear.png)

To plot data with logarithmic axes:

    python logarithmic.py

This will generate two figures:

1. self-intermediate scattering function

![logarithmic_1.png](./figure/logarithmic_1.png)

2. mean-squared displacement

![logarithmic_2.png](./figure/logarithmic_2.png)
