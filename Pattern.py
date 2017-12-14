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

# #
w_0 = 3.*1e-03 #Gaussian beam size in m
wavelenth = 555*1e-09 # in mb
Topological_charge = 1
Nodes_radial = 0 #Number of nodes in radial direction



# # LC R1080
Width = 10.56*1e-03 # im m
Resolution = 1200 #pixels


r, theta = Parts.Create_space.Generate(Width/2, Width/2, Resolution, Resolution)


amplitude = np.zeros_like(r)
phase = np.zeros_like(r)



# amplitude, phase = Parts.eq.LG_modes(r = r, theta = theta, z=0,
# 	l = Topological_charge,
# 	p = Nodes_radial,
# 	wavelenth = wavelenth,
# 	w_0 = w_0)
amplitude, phase = Parts.eq.F(r = r, theta = theta,
	l = Topological_charge,
	w_0 = w_0)

# E_0 = (1/np.max(Ampl))**2

new_phase = Parts.Code_ampl.Kotlyar(amplitude, phase)

# my_path = os.path.dirname(__file__)
# print(my_path)

# # amplitude
fig, ax = plt.subplots(1,1)
im = ax.imshow(amplitude**2, origin = 'lower', cmap=cm.gray)
plt.colorbar(im, orientation='horizontal')

# # phase
fig, ax = plt.subplots(1,1)
im = ax.imshow(phase, origin = 'lower', cmap=cm.gray)
plt.axis('off')

# # new_phase
fig, ax = plt.subplots(1,1)
im = ax.imshow(new_phase, origin = 'lower', cmap=cm.gray)
plt.axis('off')

# # # Diff
# fig, ax = plt.subplots(1,1)
# im = ax.imshow(new_phase-phase, origin = 'lower', cmap=cm.gray)
# plt.axis('off')
plt.show()


# if __name__ == '__main__':
# 	main()