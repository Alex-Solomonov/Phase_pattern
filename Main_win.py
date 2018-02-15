import sys
from PyQt4 import QtGui, QtCore
from Pattern import Calculation_pattern
import Parts
import glob
import os

lenx_px, leny_px = 250, 25

class main_frame(QtGui.QWidget):
	
	def __init__(self):
		super(main_frame, self).__init__()

		self.amplitude = 0
		self.phase = 0
		self.coded_phase = 0


		# if glob.glob('./Settings.ini'):
		# 	print('Yay!')
		# else:
			# # LC-R1080 parametrs
		self.Width_x = 16.38*1e-03 # im m
		self.Width_y = 10.56*1e-03 
		self.Resolution_x = 1920 #pixels
		self.Resolution_y = 1200 
		# # Beam par's
		self.Topological_charge = 1
		self.w_0 = 1*1e-03 #Gaussian beam size in m

		self.initUI()
		
		
	def initUI(self):      

		self.col = QtGui.QColor(0, 0, 0)

		# Generate button
		Generate = QtGui.QPushButton('Generate pattern', self)
		Generate.resize(lenx_px, leny_px)
		Generate.move(10, 10)
		# if self.phase == 0:
		# 	Generate.setStyleSheet("background-color: red")
		# else:
		# 	Generate.setStyleSheet("background-color: rgb(0,0,0)")
		Generate.clicked.connect(self.Generate)


		# Encode button
		Generate = QtGui.QPushButton('Encode', self)
		Generate.resize(lenx_px, leny_px)
		Generate.move(260, 10)
		Generate.clicked.connect(self.encode_phase)


		# Show botton
		Show_Image_i = QtGui.QPushButton('Show intensity', self)
		Show_Image_i.resize(lenx_px, leny_px)
		Show_Image_i.move(10, 55)
		Show_Image_i.clicked.connect(self.Show_I)


		Show_Image_p = QtGui.QPushButton('Show phase', self)
		Show_Image_p.resize(lenx_px, leny_px)
		Show_Image_p.move(10, 80)
		Show_Image_p.clicked.connect(self.Show_Ph)

		Show_Image = QtGui.QPushButton('Show encode phase', self)
		Show_Image.resize(lenx_px, leny_px)
		Show_Image.move(260, 80)
		Show_Image.clicked.connect(self.Show_EPh)


		# self.square = QtGui.QFrame(self)
		# self.square.setGeometry(200, 20, 960, 600)


		lbl1 = QtGui.QLabel('at the higher directory', self)
		lbl1.move(55, 105)
		# Save A**2
		Save_intensity = QtGui.QPushButton('Save intensity (in presetup folder)', self)
		Save_intensity.resize(lenx_px, leny_px)
		Save_intensity.move(10, 120)
		Save_intensity.clicked.connect(self.Save_i)

		Save_phase = QtGui.QPushButton('Save phase (in presetup folder)', self)
		Save_phase.resize(lenx_px, leny_px)
		Save_phase.move(10, 145)
		Save_phase.clicked.connect(self.Save_ph)

		Save_ephase = QtGui.QPushButton('Save encoded phase (in presetup folder)', self)
		Save_ephase.resize(lenx_px, leny_px)
		Save_ephase.move(260, 145)
		Save_ephase.clicked.connect(self.Save_eph)

		# Main window par's
		self.setGeometry(300, 150, 1200, 700)
		self.setWindowTitle('Create the pattern')
		self.show()
	
	def Generate(self):
		self.amplitude, self.phase = Calculation_pattern(self.Width_y/2,
			self.Width_x/2,
			self.Resolution_y/2,
			self.Resolution_x/2,
			l = self.Topological_charge,
			w_0 = self.w_0)

	def encode_phase(self):
		self.coded_phase = Parts.Code_ampl.Kotlyar(self.amplitude, self.phase)

	def Show_I(self):
		Parts.Image.show(self.amplitude**2)
	def Show_Ph(self):
		Parts.Image.show(self.phase)

	def Show_EPh(self):
		Parts.Image.show(self.coded_phase)

	def Save_i(self):
		Parts.Image.save(self.amplitude**2, '../list_of_figs/intens.eps')

	def Save_ph(self):
		Parts.Image.save(self.phase, '../list_of_figs/phase.eps')

	def Save_eph(self):
		Parts.Image.save(self.coded_phase, '../list_of_figs/ephase.png')