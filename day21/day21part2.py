#! /usr/bin/env python3

import scipy.optimize

#with open('test.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
	lines = fin.read().splitlines()

SYMBOLS = {}

class Symbol():
	def __init__(self, lhs, rhs):
		self.lhs = lhs
		if 1 == len(rhs):
			self.rhs = int(rhs[0])
		else:
			self.rhs = rhs
		SYMBOLS[lhs] = self

	def eval(self):
		if 'humn' == self.lhs:
			return 'x'
		rhs = self.rhs
		if int == type(rhs):
			return rhs
		else:
			x = SYMBOLS[rhs[0]].eval()
			y = SYMBOLS[rhs[2]].eval()
			if str == type(x) and 'x' not in x:
				x = int(eval(x))
			if str == type(y) and 'x' not in y:
				y = int(eval(y))
			if 'root' == self.lhs:
				#o = '=='
				o = '-'
			else:
				o = rhs[1]
			cmd = '('+str(x)+o+str(y)+')'
			if int == type(x) and int == type(y):
				z = int(eval(cmd))
			else:
				z = cmd
			self.rhs = z
			return z

	def print(self):
		print(self.lhs+' = '+str(self.rhs), type(self.rhs))

for line in lines:
	words = line.split()
	if 0 < len(words):
		lhs = words[0].strip(':')
		rhs = words[1:]
		Symbol(lhs, rhs)

root = SYMBOLS['root'].eval()
print('root = ', root)

def f(x):
	return abs(eval(root))

#
#i = -1
#run = True
#while run:
#	i += 1
#	x = f(i)
#	if x: run = False

x = scipy.optimize.fmin(f, -1)

print('Part 2:', int(x), f(x))
