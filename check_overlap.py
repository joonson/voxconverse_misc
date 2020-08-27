import pdb

with open('mapping.txt') as f:
	original = f.readlines()

with open('random.txt') as f:
	new = f.readlines()

original = [x.split(',')[0] for x in original]
new = new[0].split()

for nn in new:
	if nn in original:
		pdb.set_trace()

print('done, no overlap')