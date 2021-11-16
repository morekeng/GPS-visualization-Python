import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/arthurguy/Documents/GitHub/GPS-visualization-Python/Updated_GPS_14.csv', names=['LATITUDE', 'LONGITUDE'], sep=',', skiprows = 1)

BBox = (51.53125, -0.06740, 51.52840, -0.05841)

bethnal_g_m = plt.imread('/Users/arthurguy/Documents/GitHub/GPS-visualization-Python/map.png')

fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(df.LONGITUDE, df.LATITUDE, zorder=1, alpha= 0.2, c='b', s=10)
ax.set_title('Plotting Spatial Data on Riyadh Map')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(bethnal_g_m, zorder=0, extent = BBox, aspect= 'equal')

fig.show()