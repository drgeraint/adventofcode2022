#! /usr/bin/env python3

#puzzle = 'test'
puzzle = 'input'

with open(puzzle+'.txt', 'r') as fin:
	lines = fin.read().splitlines()

prog = puzzle+'.py'
with open(prog, 'x') as fout:
	fout.write('#! /usr/bin/env python3\n')

for line in lines:
	words = line.split()
	if 0 < len(words):
		text = 'def '+words[0].strip(':')+'():\n'
		if 2 == len(words):
			text = text+'\treturn '+words[1]+'\n'
		else:
			text = text+'\treturn '+words[1]+'() '+words[2]+words[3]+'()\n'
		with open(prog, 'a') as fout:
			fout.write(text)

with open(prog, 'a') as fout:
	fout.write('print(root())\n')
