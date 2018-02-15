import sys
from PyQt4 import QtGui, QtCore
import Parts
import glob
import os
import Main_win

lenx_px, leny_px = 250, 25
main_frame_lenx, main_frame_leny = 1200, 700
len_side_indicator = 20
space_x = space_y = 10
gap_y = 20


class Welcome(QtGui.QWidget):
	
	def __init__(self):
		super(Welcome, self).__init__()

		self.initUI()

	def initUI(self):
		self.col = QtGui.QColor(0, 0, 0)

		self.path = '../list_of_figs/'

		Ok = QtGui.QPushButton('Ok', self)
		Ok.resize(lenx_px, leny_px)
		Ok.move(space_x, space_y)
		Ok.clicked.connect(self.on_pushButton_clicked)
		self.dialog = Main_win.main_frame(self.return_preinstall_settings())



		self.setGeometry(300, 150, main_frame_lenx, main_frame_leny)
		self.setWindowTitle('Welcome!')
		self.show()

	def toMain(self):
		ex = Main_win.main_frame(self.return_preinstall_settings())

	def return_preinstall_settings(self):
		return self.path

	def on_pushButton_clicked(self):
		self.dialog.show()
		self.close()