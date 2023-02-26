import rasterio
import numpy as np
import pyvista as pv

# Load the image data from a GeoTIFF file
with rasterio.open('newZealand.tif') as src:
    img_data = src.read(1)

# Create a mesh from the image data using PyVista
mesh = pv.StructuredGrid()
mesh.dimensions = np.array([img_data.shape[0], img_data.shape[1], 1])
x, y = np.meshgrid(np.arange(mesh.dimensions[0]), np.arange(mesh.dimensions[1]))
z = img_data.flatten()
points = np.column_stack((x.flatten(), y.flatten(), z))
mesh.points = points

# Visualize the mesh using PyVista's `plot` function
mesh.plot()

