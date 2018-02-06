import os
import scipy.misc
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from Tkinter import Tk
from tkFileDialog import askopenfilename


def read():
	Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
	filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
	return scipy.misc.imread(filename)

def save(data, name):

	directory = os.path.dirname(name)
	if not os.path.exists(directory):
		os.makedirs(directory)
	scipy.misc.imsave(name, data)
	# my_path = os.path.dirname(__file__)
	# print(my_path)

def show(data):
	fig, ax = plt.subplots(1,1)
	im = ax.imshow(data, origin = 'lower', cmap=cm.gray)
	plt.colorbar(im, orientation='horizontal')

	plt.show()
	plt.close()