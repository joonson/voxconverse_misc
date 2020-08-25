import pdb, os, shutil

with open('mapping.txt','r') as f:
	lines = f.readlines()

maps = {}

for line in lines:
	shutil.copyfile('voxconv_dev_14_spk_voxconv/%s.rttm'%(line.strip().split(',')[0]),'original/%s.rttm'%(line.strip().split(',')[1]))

