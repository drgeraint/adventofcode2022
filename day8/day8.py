#! /usr/bin/env python3

import numpy as np

#with open('test.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
	lines = fin.read().splitlines()

rows = []
for line in lines:
	col = []
	for c in line:
		col.append(int(c))
	rows.append(col)

data = np.array(rows)

vizt = np.empty(data.shape)     # top
vizb = np.empty(data.shape)     # bottom
vizl = np.empty(data.shape)     # left
vizr = np.empty(data.shape)     # right
viz  = np.empty(data.shape)

nrows = data.shape[0]
ncols = data.shape[1]

for row in range(0, nrows):
	for col in range(0, ncols):
                # visibility from top
		if 0 == row:
			vizt[row,col] = True
		elif data[row,col] > max(data[:row,col]):
			vizt[row,col] = True
		else:
			vizt[row,col] = False

                # visibility from bottom
		if nrows-1 == row:
			vizb[row,col] = True
		elif data[row,col] > max(data[row+1:,col]):
			vizb[row,col] = True
		else:
			vizb[row,col] = False

                # visibility from left
		if 0 == col:
			vizl[row,col] = True
		elif data[row,col] > max(data[row,:col]):
			vizl[row,col] = True
		else:
			vizl[row,col] = False

                # visibility from right
		if ncols-1 == col:
			vizr[row,col] = True
		elif data[row,col] > max(data[row,col+1:]):
			vizr[row,col] = True
		else:
			vizr[row,col] = False

                # overall visibility
		viz[row,col] = vizt[row,col] or vizb[row,col] or vizl[row,col] or vizr[row,col]

print('Part 1:', int(viz.sum()))


scenic_view = np.empty(data.shape)

for row in range(0, nrows):
        for col in range(0, ncols):
                view = {}
                view['t'] = np.flip(data[:row,col])
                view['b'] = data[row+1:,col]
                view['l'] = np.flip(data[row,:col])
                view['r'] = data[row,col+1:]

                scene = []
                for k, v in view.items():
                        i = np.where(v >= data[row,col])[0]
                        if len(i) > 0:
                                val = i[0]+1
                        else:
                                val = len(v)
                        scene.append(val)
                scenic_view[row,col] = np.product(scene)

print('Part 2:', int(max(np.reshape(scenic_view,nrows*ncols,1))))
                
