import pdb, os, shutil

with open('../spottheconversation/mapping_test.txt','r') as f:
	lines = f.readlines()

maps = {}

linesplit = [[x.split(',')[0],x.split(',')[1].strip()] for x in lines]

with open('all.rttm','w') as h:
	for lidx, line in enumerate(linesplit):
		with open('results/%s.rttm'%(line[0])) as f:
			flines = f.readlines()

		with open('original_test/%s.rttm'%(line[1]),'w') as g:
			for fline in flines:
				g.write('%s'%(fline.replace(' '+line[0]+' ',' '+line[1]+' ')))
				h.write('%s'%(fline.replace(' '+line[0]+' ',' '+line[1]+' ')))



