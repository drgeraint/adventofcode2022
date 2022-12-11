#! /usr/bin/env python3

#filename = 'input.txt'
filename = 'test.txt'
PART = 2

import numpy as np

MONKEYS = []

class Monkey:
    def __init__(self, monkey_def):
        num_def      = monkey_def[0]
        items_def    = monkey_def[1]
        op_def       = monkey_def[2]
        test_def     = monkey_def[3]
        target_T_def = monkey_def[4]
        target_F_def = monkey_def[5]
        self.activity = 0
        self.num = num_def.split()[1]        
        self.items = []
        for item in items_def.split()[2:]:
            self.items.append(int(item))
        self.op = ''
        for word in op_def.split()[3:]:
            self.op = self.op + word
        self.divisor  = int(test_def.split()[3])
        self.target_T = int(target_T_def.split()[5])
        self.target_F = int(target_F_def.split()[5])

    def print(self):
        print('Monkey', self.num, 'Activity', self.activity, 'Items', self.items)

    def update(self):
        while 0 < len(self.items):
            self.activity = self.activity + 1
            old = self.items.pop(0)
            x = eval(self.op)
            if 1 == PART:
                x = int(np.floor(x/3))
            if 0 == np.mod(x, self.divisor):
                target = self.target_T
            else:
                target = self.target_F
            # print(old, '->', x, '->', target)
            MONKEYS[target].items.append(x)
            
with open(filename, 'r') as fin:
    lines = fin.read().splitlines()
    nlines = len(lines)
    for i in range(0, nlines):
        lines[i] = lines[i].translate({ord(':'):ord(' '), ord(','):ord(' ')}) 
        lines[i] = lines[i].strip()
    for i in range(0, int(np.floor(nlines/7)+1)):
        monkey_def = lines[i*7:i*7+6]
        MONKEYS.append(Monkey(monkey_def))

for m in MONKEYS:
    m.print()

if 1 == PART:
    nrounds = 20
elif 2 == PART:
    nrounds = 10000
    
for round in range(0,nrounds):            
    if 0 == np.mod(round, 200):
        print('Round', round)
    for m in MONKEYS:
        m.update()

for m in MONKEYS:
    m.print()
        
activities = []
for m in MONKEYS:
    activities.append(m.activity)

m0 = max(activities)
activities.remove(m0)
m1 = max(activities)
print('Part 1:', m0*m1)
