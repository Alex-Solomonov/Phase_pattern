from PyQt5.QtCore import QDir, Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import functools
import Parts

class RenderArea(QWidget):
	def __init__(self, parent=None):
		super(RenderArea, self).__init__(parent)
		self.setBackgroundRole(QPalette.Midlight)
		self.setAutoFillBackground(True)



		

class Main_frame(QDialog):
	"""docstring for Main_frame"""
	def __init__(self, SLM_pars, Beam_pars):
		super(Main_frame, self).__init__()
		self.SLM_pars = SLM_pars
		self.Beam_pars = Beam_pars

		self.init_text()
		self.create_Beam_Group_box()
		self.create_Encode_Group_box()

		# RenderArea = RenderArea

		mainLayout = QVBoxLayout()
		mainLayout.addWidget(self.Beam_Group_box)
		mainLayout.addWidget(self.Encode_Group_box)

		self.setLayout(mainLayout)

		self.setWindowTitle("Main page")
	
	def init_text(self):
		self.Amplitude_Label_button = ["Create amplitude and phase",\
			"Read amplitude from image"]

		self.Amplitude_Label = ["Bessel max(A) = 1",\
			"Bessel max(A) = 2",\
			"Hollow Gauss",\
			"Hollow rectangle",\
			"Square"]

		self.Encode_Label_Button = "Encode field"

		self.Encode_Label = ["Kotlyar",\
			"Fuentes",\
			"IFTA"]
		self.Show_n_Save = ["Show amplitude",\
			"Show phase"]

	def btnPressed(self, idx):
		if idx == self.Amplitude_Label_button[0]:
			self.Coordinates = Parts.Create_space.Generate(self.SLM_pars)
			self.Field = Parts.Field_equation.Bessel_max_at_2(\
				self.Coordinates, self.Beam_pars)

		if idx == self.Amplitude_Label_button[1]:
			pass

		if idx == self.Encode_Label_Button:
			self.Encoded_field = Parts.Encode_field.Kotlyar(self.field)


	def create_Beam_Group_box(self):
		self.Beam_Group_box = QGroupBox("Create field")
		layout = QGridLayout()

		for i in range(len(self.Amplitude_Label)):
			Radio = QRadioButton(self.Amplitude_Label[i])
			layout.addWidget(Radio, i, 0)

		for i in range(len(self.Amplitude_Label_button)):
			button = QPushButton(self.Amplitude_Label_button[i])
			layout.addWidget(button,len(self.Amplitude_Label)+1,i)

			# connect
			button.clicked.connect(\
				functools.partial(self.btnPressed,\
					self.Amplitude_Label[i]))
		self.Beam_Group_box.setLayout(layout)
	
	def RadioPressed(self, idx):
		pass
				
	def create_Encode_Group_box(self):
		self.Encode_Group_box = QGroupBox("Encode field")
		layout = QGridLayout()
		
		for i in range(len(self.Encode_Label)):
			Radio = QRadioButton(self.Encode_Label[i])
			layout.addWidget(Radio, i, 0)

		button = QPushButton(self.Encode_Label_Button)
		button.clicked.connect(self.btnPressed)
		layout.addWidget(button, len(self.Encode_Label)+1 , 0)
		
		self.Encode_Group_box.setLayout(layout)