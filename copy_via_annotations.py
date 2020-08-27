import glob, pdb, shutil
from shutil import copyfile

srcdir = 'backup/vgginternal/vox-converse-annotation/store/via-3.x.y/rev'
tgtdir = 'annotations'

f = open('voxconverse.csv','r')
lines = f.readlines()
f.close()

for line in lines[1:]:
	fields = line.split(',')
	yref = fields[1]
	vref = fields[2]

	files = glob.glob('%s/%s/*.json'%(srcdir,vref))

	src = '%s/%s/rev-%d.json'%(srcdir,vref,len(files))
	tgt = '%s/%s.json'%(tgtdir,yref)

	copyfile(src,tgt)
	print('Copied %s'%tgt)
