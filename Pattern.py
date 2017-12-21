# encoding=utf8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

import numpy as np

import Parts

def Calculation_pattern(x_max, y_max, Resolution_x, Resolution_y, l, w_0):
	# # Creation Calc Space

	r, theta = Parts.Create_space.Generate(x_max, y_max, Resolution_x, Resolution_y)
	
	amplitude = np.zeros_like(r)
	phase = np.zeros_like(r)
	
	amplitude, phase = Parts.eq.Bessel(r/w_0, theta, l)
	amplitude = Parts.eq.Square(r)

	new_phase = Parts.Code_ampl.Kotlyar(amplitude, phase)

	# Parts.Image.show(amplitude**2)
	# Parts.Image.show(phase)
	Parts.Image.show(new_phase)
	Parts.Image.save(new_phase, '../list_of_figs/sq_phase.png')

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
	Resolution_y/2,
	Resolution_x/2,
	l = Topological_charge,
	w_0 = w_0)
