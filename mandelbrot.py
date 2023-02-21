import numpy as np
import matplotlib.pyplot as plt

# Set up a grid of complex numbers representing the points in the image
xmin, xmax, xstep = -2.0, 1.0, 0.005
ymin, ymax, ystep = -1.5, 1.5, 0.005
x, y = np.meshgrid(np.arange(xmin, xmax, xstep), np.arange(ymin, ymax, ystep))
c = x + 1j*y

# Calculate the Mandelbrot set using a loop
z = np.zeros_like(c)
for i in range(100):
    z = z**2 + c

# Create an image of the Mandelbrot set
mandelbrot = np.abs(z) < 2
plt.imshow(mandelbrot.T, cmap='binary', extent=[xmin, xmax, ymin, ymax])
plt.axis('off')
plt.show()
