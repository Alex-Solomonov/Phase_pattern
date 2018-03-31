from PyQt5.QtCore import QDir, Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

class Main_frame(QMainWindow):
	"""docstring for Main_frame"""
	def __init__(self, SLM_pars, Beam_pars):
		super(Main_frame, self).__init__()
		self.SLM_pars = SLM_pars
		self.Beam_pars = Beam_pars

		print(self.SLM_pars)