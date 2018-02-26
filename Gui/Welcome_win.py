import sys
from PyQt4 import QtGui, QtCore
import Parts
import glob
import os
import Main_win

lenx_px, leny_px = 100, 25
main_frame_lenx, main_frame_leny = 1200, 700
len_side_indicator = 20
space_x = space_y = 10
gap_y = 20


class Welcome(QtGui.QMainWindow):
	
	def __init__(self):
		super(Welcome, self).__init__()

		self.initUI()

	def initUI(self):
		self.col = QtGui.QColor(0, 0, 0)

		if glob.glob('./Settings.ini'):

			self.path = '../list_of_figs/'

			Yes = QtGui.QPushButton('Yes', self)
			Yes.resize(lenx_px, leny_px)
			Yes.move(space_x, space_y)
			Yes.clicked.connect(self.on_pushButton_clicked)

			No = QtGui.QPushButton('No, use default', self)
			No.resize(lenx_px, leny_px)
			No.move(space_x+lenx_px, space_y)
			No.clicked.connect(self.on_pushButton_clicked)
			self.dialog = Main_win.main_frame(self.return_preinstall_settings())

		else:
			self.close()

		self.setGeometry(300, 150, main_frame_lenx, main_frame_leny)
		self.setWindowTitle('Welcome!')

		

	def toMain(self):
		ex = Main_win.main_frame(self.return_preinstall_settings())

	def return_preinstall_settings(self):
		return self.path

	def on_pushButton_clicked(self):
		self.dialog.show()
		self.close()