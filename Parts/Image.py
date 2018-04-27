import os
from scipy import misc, ndimage

import matplotlib.pyplot as plt
import matplotlib.cm as cm

def save(data, name):
	directory = os.path.dirname(name)
	if not os.path.exists(directory):
		os.makedirs(directory)
	misc.imsave(name, data)
	# my_path = os.path.dirname(__file__)
	# print(my_path)

def show(data):
	fig, ax = plt.subplots(1,1)
	im = ax.imshow(data, origin = 'lower', cmap=cm.gray)
	plt.colorbar(im, orientation='horizontal')

	plt.show()
	plt.close()

def read(name):
	Raw_image = ndimage.imread(name, flatten = True)
	# print(Raw_image.dtype)
	return Raw_image
