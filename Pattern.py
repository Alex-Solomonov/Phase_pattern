# encoding=utf8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')	

import numpy as np

import Parts

def Calculation_pattern(x_max, y_max, Resolution_x, Resolution_y, l, w_0):
	# Creation Calc Space
	r, theta = Parts.Create_space.Generate(x_max, y_max, Resolution_x, Resolution_y)
	
	amplitude = np.zeros_like(r)
	phase = np.zeros_like(r)
	
	amplitude, phase = Parts.eq.Bessel(r/w_0, theta, l)
	new_phase = Parts.Code_ampl.Kotlyar(amplitude, phase)

	return amplitude, phase
	# a, ph = Parts.Misc.interference(r/w_0, amplitude, phase)
	# Parts.Image.show(amplitude**2)
	# Parts.Image.save(amplitude**2, '../list_of_figs/intens.eps')
	# Parts.Image.show(phase)
	# Parts.Image.save(phase, '../list_of_figs/phase.eps')
	# Parts.Image.show(new_phase)
	# Parts.Image.show(Parts.Misc.Move(new_phase, 65, 40))
	# Parts.Image.save(Parts.Misc.Move(new_phase, 0, 0), '../list_of_figs/HG.png')

if __name__ == '__main__':
	# # LC-R1080 parametrs
	Width_x = 16.38*1e-03 # im m
	Width_y = 10.56*1e-03 
	Resolution_x = 1920 #pixels
	Resolution_y = 1200 

	# # Beam par's
	Topological_charge = 1
	w_0 = 1*1e-03 #Gaussian beam size in m

	Calculation_pattern(Width_y/2,
		Width_x/2,
		Resolution_y/2,
		Resolution_x/2,
		l = Topological_charge,
		w_0 = w_0)