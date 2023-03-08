from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def plot_image_colors(image: Image.Image):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    arr = np.array(image)
    xdata = arr[:, :, 0].reshape(-1, 1)
    ydata = arr[:, :, 1].reshape(-1, 1)
    zdata = arr[:, :, 3].reshape(-1, 1)
    cdata = arr.reshape(-1, 3)

    ax.scatter3D(xdata, ydata, zdata, c=cdata, cmap='Greens');
