#! /usr/bin/env python3

import numpy as np

signal = [1]

#with open('test.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
	lines = fin.read().splitlines()

for line in lines:
    words = line.split()
    x = signal[-1]
    signal.append(x)
    command = words[0]
    if 'addx' == command:
        v = int(words[1])
        signal.append(x+v)

trace = np.array(signal)
score = 20*trace[19]+60*trace[59]+100*trace[99]+140*trace[139]+180*trace[179]+220*trace[219]
print(score)

crt = ''
for i in range(0,len(trace)):
    x = trace[i]
    j = np.mod(i, 40)
    if j-1 == x or j == x or j+1 == x:
        lit = '#'
    else:
        lit = '.'
    crt = crt + lit
    if 39 == j:
        print(crt)
        crt = ''

