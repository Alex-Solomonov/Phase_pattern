# import Gui
import sys
from PyQt4 import QtGui
import Gui

def main():
	
	app = QtGui.QApplication(sys.argv)
	w = Gui.Welcome_win.Welcome()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()	