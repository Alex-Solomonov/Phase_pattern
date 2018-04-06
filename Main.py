if __name__ == '__main__':

	import sys
	import glob
	import Gui
	print(sys.version)
	from PyQt5.QtWidgets import QApplication

	app = QApplication(sys.argv)

	if glob.glob('Settings.ini'):
		state, SLM_pars, Beam_pars = Gui.Initial.read_settings()
		if state == 1:
			dialog = Gui.Main_window.Main_frame(SLM_pars, Beam_pars)
		else:
			dialog = Gui.Intro(arg = True)
	else:
		dialog = Gui.Intro(arg = False)

	sys.exit(dialog.exec_())