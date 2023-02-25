from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt

# you can replace the exisiting .tif file with anything want to geo-analyzed / plotted! 
dataset = gdal.Open('land_shallow_topo_8192.tif')

raster_data = dataset.ReadAsArray()

num_bands = dataset.RasterCount
print('Number of bands: {}'.format(num_bands))

width = dataset.RasterXSize
height = dataset.RasterYSize
print('Size:', width, 'x', height)
pixel_width, pixel_height = dataset.GetGeoTransform()[1:3]
print('Pixel size:', pixel_width, 'x', pixel_height)

# extract the red channel
raster_data = raster_data[0]

# reshape the data into a 2d array
raster_data = raster_data.reshape((height, width))

plt.imshow(raster_data, cmap='gray')
plt.show()

