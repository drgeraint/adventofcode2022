#! /usr/bin/env python3

import numpy as np

#puzzle = 'test'
puzzle = 'input'

MAP = {'2':2, '1':1, '0':0, '-':-1, '=':-2,
       2:'2', 1:'1', 0:'0', -1:'-', -2:'=' }

def snafu2dec(s):
	n = len(s)
	total = 0
	for i in range(0, n):
		j = n-i-1
		total += MAP[s[j]]*pow(5, i)
	return total

def logn(d, n):
	v = int(d)
	val = np.log(v) / np.log(n)
	return val

def dec2base(d, b):
	v = int(d)
	try:
		n = 1+int(logn(v, b))
	except:
		print('v:', v, 'b:', b)
	val = ''
	for i in range(0, n):
		j = n-i-1
		x = str(int(v / (pow(b, j))) % b)
		val += x
	return val

def dec2snafu(d):
	v = ' '+dec2base(d, 5)
	v = list(v)
	n = len(v)
	for i in range(1, n):
		j = n-i
		x = int(v[j])
		a = x % 3 
		b = int(x / 3)
		if b > 0:
			v[j] = MAP[a-2]
			if 1 == j:
				v[j-1] = 1
			else:
				v[j-1] = int(v[j-1])+1
		else:
			v[j] = MAP[a]
	val = ''
	for i in range(0, n):
		val += str(v[i])
	val = val.strip(' ')
	return val
	

if 'test' == puzzle:
	with open('tests-snafu2dec.txt', 'r') as f:
		lines = f.read().splitlines()

	for x in [1, 2, 3, 9, 10, 11, 19, 99, 100, 101, 11500293060236 ]:
		y = dec2base(x, 10)
		try:
			assert(int(y) == x)
		except AssertionError as e:
			print(x, type(x), y, type(y))
			raise e

	for line in lines:
		if 0 < len(line):
			s, val = line.split()
			d = snafu2dec(s)
			try:
				assert(snafu2dec(s) == int(val))
			except AssertionError as e:
				print('s:',s, 'd:', d, 'val:', val)
				raise e

	with open('tests-dec2snafu.txt', 'r') as f:
		lines = f.read().splitlines()
	for line in lines:
		if 0 < len(line):
			d, val = line.split()
			s = dec2snafu(d)
			try:
				assert(dec2snafu(d) == val)
			except AssertionError as e:
				print('s:',s, 'd:', d, 'val:', val)
				raise e



with open(puzzle+'.txt', 'r') as f:
	lines = f.read().splitlines()


data = []
for s in lines:
	if 0 < len(s):
		d = snafu2dec(s)
		t = dec2snafu(d)
		try:
			assert(s == t)
		except:
			print('s:', s, type(s), 'd:', d, type(d), 't:', t, type(t))
		data.append(int(d))

for i in range(0, len(data)):
	s = dec2snafu(data[i])
	assert( s == lines[i] )

print('Part 1:', dec2snafu(sum(data)))

#print(max(data))
