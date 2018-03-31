if __name__ == '__main__':

	import sys
	import glob
	import Gui
	from PyQt5.QtWidgets import QApplication

	app = QApplication(sys.argv)

	if glob.glob('./Setting.ini'):
		dialog = Gui.Intro(arg = True)
	else:
		dialog = Gui.Intro(arg = False)
	
	sys.exit(dialog.exec_())
