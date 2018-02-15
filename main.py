# import Gui
import sys
from PyQt4 import QtGui
import Main_win

def main():
	
	app = QtGui.QApplication(sys.argv)
	ex = Main_win.main_frame()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()