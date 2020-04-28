import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = plt.figure()

ax=fig.gca(projection='3d')
x,y,z = axes3d.get_test_data(0.10)
#graf = ax.contourf(x,y,z)
graf = ax.plot_wireframe(x,y,z)
