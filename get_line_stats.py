import pdb, os, glob

files = glob.glob('annotations/*.rttm')

for file in files:
	with open(file) as f:
		lines = f.readlines()
	ids = len(list(set([x.split()[-3] for x in lines])))
	duration = max([float(x.split()[3]) + float(x.split()[4]) for x in lines])
	numlines = len(lines)

	print(os.path.basename(file).split('.')[0],ids,duration,numlines)