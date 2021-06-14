import matplotlib.pyplot as plt
import time
import numpy as np
from dynamic_plotter.dyn_plotter import dyn_plotter


fig1, ax1 = plt.subplots()
fig1.suptitle("Live Logging Quantity 1", fontsize=16)
ax1.set_xlabel("Time / [s]")
ax1.set_ylabel("Voltage / [V]")
ax1.grid()
dl1 = dyn_plotter.dynamicPlotter(fig1, windowSize=20, lineStyle="g-")

fig2, ax2 = plt.subplots()
fig2.suptitle("Live Logging Quantity 2", fontsize=16)
ax2.set_xlabel("Time / [s]")
ax2.set_ylabel("Voltage / [V]")
ax2.grid()
dl2 = dyn_plotter.dynamicPlotter(fig2)

i = 0
j = 0
while True:
    y = 3*np.sin(20*j) + 10*j
    dl1.add_data(j, y)
    dl2.add_data(j, y+10)
    i += 1
    j += 0.01
    time.sleep(0.01)