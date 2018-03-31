from PyQt5.QtWidgets import *
import functools
import Gui


class Intro(QDialog):
	def __init__(self, arg):
		super(Intro, self).__init__()
		self.arg = arg

		self.init_text()
		self.create_SLM_parametes_Group_box()
		self.create_Beam_parameters_Group_box()
		self.create_Button_Group_box()

		
		mainLayout = QVBoxLayout()

		mainLayout.addWidget(self.label)
		mainLayout.addWidget(self.SLM_parametes_Group_box)
		mainLayout.addWidget(self.Beam_parameters_Group_box)
		mainLayout.addWidget(self.horizontal_Button_box)

		self.setLayout(mainLayout)

		self.setWindowTitle("Introduction")



	def init_text(self):
		self.Label_button = ["No, use default for LC-R1080",\
				"0"]
		print(self.arg)
		if self.arg == True:
			self.label = QLabel("Hi! I find config files\n\
			"
			)
			self.Label_button[1] = "Yes, use this parameters"
		else:
			self.label = QLabel("Hi! I didn't find any config files\n\
			"
			)
			self.Label_button[1] = "Yes, create own parameters"

		self.Label_SLM_pars = ["Y width",\
				"X width",\
				"Y resolution",\
				"X resolution"]
		self.Label_SLM_pars_base_units = ["m", "points"]

		self.Label_Beam_pars = ["Topological charge",\
			"FWHM"]
		self.Label_Beam_pars_base_units = [" ",\
			"m"]

		self.Default_parameters()

	def Default_parameters(self):
		# Width_y, Width_x, Resolution_y, Resolution_x
		self.SLM_pars = [16.38*1e-03,\
			10.53*1e-03,\
			1980,\
			1200]
		# Topological charge, FWHM
		self.Beam_pars = [1,\
			124 * min([self.SLM_pars[0]/self.SLM_pars[2],\
				 self.SLM_pars[1]/self.SLM_pars[3]])]

	def create_SLM_parametes_Group_box(self):
		self.SLM_parametes_Group_box = QGroupBox()
		layout = QGridLayout()

		for i in range(len(self.Label_SLM_pars)):
			name_label = QLabel(self.Label_SLM_pars[i])
			value_label = QLabel("%f" % self.SLM_pars[i])
			unit_label = QLabel(self.Label_SLM_pars_base_units[i//2])
			lineEdit = QLineEdit()
			layout.addWidget(name_label, i, 0)
			layout.addWidget(value_label, i, 1)
			layout.addWidget(unit_label, i, 2)
			layout.addWidget(lineEdit, i, 3)

		layout.setColumnStretch(1, 10)
		layout.setColumnStretch(2, 20)


		self.SLM_parametes_Group_box.setLayout(layout)

	def create_Button_Group_box(self):
		self.horizontal_Button_box = QGroupBox()
		layout = QGridLayout()

		Warning_label = ["* Clicking 'yes' will create", \
			"the 'Settings.ini' file."]
		self.Button_list = []

		for i in range(len(self.Label_button)):
			button = QPushButton(self.Label_button[i])
			self.Button_list.append(button)
			Warning_layout = QLabel(Warning_label[i])
			layout.addWidget(button, 0, i)
			layout.addWidget(Warning_layout, 1, i)

			# connect
			button.clicked.connect(\
				functools.partial(self.btnPressed,self.Label_button[i]))

		self.horizontal_Button_box.setLayout(layout)

	def create_Beam_parameters_Group_box(self):
		self.Beam_parameters_Group_box=QGroupBox()
		layout = QGridLayout()

		for i in range(len(self.Beam_pars)):
			name_label = QLabel(self.Label_Beam_pars[i])
			value_label = QLabel("%f" % self.Beam_pars[i])
			unit_label = QLabel(self.Label_Beam_pars_base_units[i])
			lineEdit = QLineEdit()
			layout.addWidget(name_label, i, 0)
			layout.addWidget(value_label, i, 1)
			layout.addWidget(unit_label, i, 2)
			layout.addWidget(lineEdit, i, 3)

		self.Beam_parameters_Group_box.setLayout(layout)

	def btnPressed(self, idx):
		# No, use default for LC-R1080
		if idx == self.Label_button[0]:
			self.main = Gui.Main_frame()
			self.close()
			self.main.show()
		if idx == self.Label_button[1] and self.arg == True:
			self.SLM_pars, self.Beam_pars = read_settings()
			self.main = Gui.Main_frame()
			self.close()
			self.main.show()
		else:
			create_settings(self.SLM_pars, self.Beam_pars)
			self.main = Gui.Main_frame()
			self.close()
			self.main.show()
		

def create_settings(SLM_pars, Beam_pars):
		# create_settings(self.SLM_pars, self.Beam_pars)
	Mask_SLM = ['Width_y',\
		'Width_x',\
		'Resolution_y',\
		'Resolution_x']
	Mask_Beam = ['Topological_charge',\
		'FWHM']

	with open('Settings.ini', 'w') as f:
		f.write("# Known parameters of spatial light modulator\n")
		for i in range(len(SLM_pars)):
			f.write("{} = {}\n".format(Mask_SLM[i], SLM_pars[i]))
		f.write("\n# Parameters of beam\n")
		for i in range(len(Beam_pars)):
			f.write("{} = {}\n".format(Mask_Beam[i], Beam_pars[i]))

def read_settings():
	with open('Settings.ini', 'r') as f:
		raw = f.read()
	
	raw = raw.split('\n')
	for i in range(raw.count('')):
		raw.remove('')
	for line in raw:
		if line[0] == '#':
			raw.remove(line)
	cooked = []
	for line in raw:
		line = line.split(' ')
		cooked.append(line[-1])

	SLM_pars = cooked[0:4]
	Beam_pars = cooked[4:6]
	
	return SLM_pars, Beam_pars
