import sys
from PyQt4 import QtGui, QtCore
from Pattern import Calculation_pattern
import Parts
import glob
import os

lenx_px, leny_px = 250, 25
main_frame_lenx, main_frame_leny = 1200, 700
len_side_indicator = 20


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
		Generate.clicked.connect(self.Generate)
		Generate.clicked.connect(self.setColor)


		# Encode button
		Generate = QtGui.QPushButton('Encode', self)
		Generate.resize(lenx_px, leny_px)
		Generate.move(260, 10)
		Generate.clicked.connect(self.encode_phase)



		# Show botton
		Show_Image_i = QtGui.QPushButton('Show intensity', self)
		Show_Image_i.resize(lenx_px, leny_px)
		Show_Image_i.move(10, 55)
		Show_Image_i.clicked.connect(self.Show)


		Show_Image_p = QtGui.QPushButton('Show phase', self)
		Show_Image_p.resize(lenx_px, leny_px)
		Show_Image_p.move(10, 80)
		Show_Image_p.clicked.connect(self.Show)

		Show_Image = QtGui.QPushButton('Show encode phase', self)
		Show_Image.resize(lenx_px, leny_px)
		Show_Image.move(260, 80)
		Show_Image.clicked.connect(self.Show)




		lbl1 = QtGui.QLabel('at the higher directory', self)
		lbl1.move(55, 105)
		# Save A**2
		Save_intensity = QtGui.QPushButton('Save intensity (in presetup folder)', self)
		Save_intensity.resize(lenx_px, leny_px)
		Save_intensity.move(10, 120)
		Save_intensity.clicked.connect(self.Save)

		Save_phase = QtGui.QPushButton('Save phase (in presetup folder)', self)
		Save_phase.resize(lenx_px, leny_px)
		Save_phase.move(10, 145)
		Save_phase.clicked.connect(self.Save)

		Save_ephase = QtGui.QPushButton('Save encoded phase (in presetup folder)', self)
		Save_ephase.resize(lenx_px, leny_px)
		Save_ephase.move(260, 145)
		Save_ephase.clicked.connect(self.Save)



		self.square1 = QtGui.QFrame(self)
		self.square1.setGeometry(10, main_frame_leny-len_side_indicator-10, len_side_indicator, len_side_indicator)
		self.square1.setStyleSheet("QWidget { background-color: red}")

		# Main window par's
		self.setGeometry(300, 150, main_frame_lenx, main_frame_leny)
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

	def Show(self):
		source = self.sender()
		if source.text() == 'Show intensity':
			Parts.Image.show(self.amplitude**2)
		elif source.text() == 'Show phase':
			Parts.Image.show(self.phase)
		elif source.text() == 'Show encoded phase':
			Parts.Image.show(self.coded_phase)

	def Save(self):
		source = self.sender()		
		if source.text() == 'Save intensity (in presetup folder)':
			Parts.Image.save(self.amplitude**2, '../list_of_figs/intens.eps')
		elif source.text() == 'Save phase (in presetup folder)':
			Parts.Image.save(self.phase, '../list_of_figs/phase.eps')
		elif source.text() == 'Save encoded phase (in presetup folder)':
			Parts.Image.save(self.coded_phase, '../list_of_figs/ephase.png')
		
	def setColor(self):
		source = self.sender()

		if source.text() == 'Generate pattern':
			self.square1.setStyleSheet("QFrame { background-color: green}")  