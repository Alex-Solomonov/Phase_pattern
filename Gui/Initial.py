def create_settings(SLM_pars, Beam_pars, state):
		# create_settings(self.SLM_pars, self.Beam_pars)
	Mask_SLM = ['Width_y',\
		'Width_x',\
		'Resolution_y',\
		'Resolution_x']
	Mask_Beam = ['Topological_charge',\
		'FWHM']

	with open('Settings.ini', 'w') as f:
		f.write("Dont_show_this_again = {}\n".format(state))
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
	# Remove #-like commentaries
	for i in range(raw.count('')):
		raw.remove('')
	for line in raw:
		if line[0] == '#':
			raw.remove(line)

	# Read parameters
	undercooked = []
	for line in raw:
		line = line.split(' ')
		undercooked.append(line[-1])

	cooked = []
	for item in undercooked:
		cooked.append(float(item))

	state = cooked[0]
	SLM_pars = cooked[1:5]
	Beam_pars = cooked[5:7]
	
	return  state, SLM_pars, Beam_pars