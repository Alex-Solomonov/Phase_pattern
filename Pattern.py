# encoding=utf8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

import os
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

import Parts

def Calculation_pattern(x_max, y_max, Resolution_x, Resolution_y, l, w_0):
	# # Creation Calc Space
	r, theta = Parts.Create_space.Generate(x_max, y_max, Resolution_x, Resolution_y)
	
	amplitude = np.zeros_like(r)
	phase = np.zeros_like(r)
	
	amplitude, phase = Parts.eq.Bessel(r/w_0, theta, l)

	new_phase = Parts.Code_ampl.Kotlyar(amplitude, phase)

	# # amplitude
	im = plt.matshow(amplitude**2, cmap = cm.gray)
	plt.colorbar(im, orientation='horizontal')

	sizes = np.shape(phase)
	print(sizes)
	fig = plt.figure()
	fig.set_size_inches(1. * sizes[0] / sizes[1], 1, forward = False)
	ax = plt.Axes(fig, [0., 0., 1., 1.])
	ax.set_axis_off()
	fig.add_axes(ax)
	im = ax.imshow(phase, cmap=cm.gray)

	sizes = np.shape(phase)
	fig = plt.figure()
	fig.set_size_inches(1. * sizes[0] / sizes[1], 1, forward = False)
	ax = plt.Axes(fig, [0., 0., 1., 1.])
	ax.set_axis_off()
	fig.add_axes(ax)
	im = ax.imshow(new_phase, cmap=cm.gray)
	plt.savefig('phase.png', dpi = sizes[0], cmap=cm.gray, bbox_inches='tight')
	# plt.savefig('phase.png', dpi = sizes[0], cmap=cm.gray, bbox_inches='tight')


	plt.show()
# # my_path = os.path.dirname(__file__)
# # print(my_path)

if __name__ == '__main__':
	# # LC-R1080 parametrs
	Width_x = 16.38*1e-03 # im m
	Width_y = 10.56*1e-03 
	Resolution_x = 1920 #pixels
	Resolution_y = 1200 

	# # Beam parametr
	Topological_charge = 1
	w_0 = 1.5*1e-03 #Gaussian beam size in m

	Calculation_pattern(Width_y/2,
	Width_x/2,
	Resolution_y,
	Resolution_x,
	l = Topological_charge,
	w_0 = w_0)