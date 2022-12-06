#! /usr/bin/env python3

import copy

#with open('test.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

read_columns1 = [[]]
columns1 = []
columns2 = []

Az = set()
for i in range(ord('a'), ord('z')+1):
    Az.add(chr(i))
for i in range(ord('A'), ord('Z')+1):
    Az.add(chr(i))

building_stack = True
for line in lines:
    if building_stack and len(line) is 0:
        building_stack = False
        for col in read_columns1:
            columns1.append(list(reversed(col)))
        columns2 = copy.deepcopy(columns1) 
    elif building_stack:
        n = len(line.rstrip())
        col = 0
        i = 1
        while (i < n):
            c = line[i]
            if c in Az:
                while col >= len(read_columns1):
                    read_columns1.append([])
                read_columns1[col].append(c)
            col = col + 1
            i = 1 + 4*col
    else:                       # instructions
        instructions = line.split(' ')
        num = int(instructions[1])
        src = int(instructions[3])-1
        dst = int(instructions[5])-1
        
        for i in range(0, num):
            x = columns1[src].pop()
            columns1[dst].append(x)

        y = columns2[src][-num:]
        columns2[src] = columns2[src][:-num]
        for c in y:
            columns2[dst].append(c)
        
        
tops1 = ''
for col in columns1:
    tops1 = tops1+col[-1]
print('Part 1:', tops1)

tops2 = ''
for col in columns2:
    if len(col) > 0:
        ctop2 = col[-1]
    else:
        ctop2 = ' '
    tops2 = tops2+ctop2
print('Part 2:', tops2)
