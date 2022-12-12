#! /usr/bin/env python3

import sys
import divisible as my

#sys.setrecursionlimit(100000)

filename = 'input.txt'
#filename = 'test.txt'
PART = 2

MONKEYS  = []
DIVISORS = set()
COMMON   = 1

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
        DIVISORS.add(self.divisor)
        self.target_T = int(target_T_def.split()[5])
        self.target_F = int(target_F_def.split()[5])

    def print(self):
        print('Monkey', self.num, 'Activity', self.activity, 'Items', self.items)

    def update(self):
        if 0 < len(self.items):
            self.activity = self.activity + len(self.items)
            for old in self.items:
                x = eval(self.op) # op is f(old)
                if 1 == PART:
                    x = int(x/3)
                x = x % COMMON
                if 0 == x % self.divisor:
                #if my.divisible(x, self.divisor):
                    target = self.target_T
                else:
                    target = self.target_F
                MONKEYS[target].items.append(x)
            self.items = []
            
with open(filename, 'r') as fin:
    lines = fin.read().splitlines()
    nlines = len(lines)
    for i in range(0, nlines):
        lines[i] = lines[i].translate({ord(':'):ord(' '), ord(','):ord(' ')}) 
        lines[i] = lines[i].strip()
    for i in range(0, int(nlines/7+1)):
        monkey_def = lines[i*7:i*7+6]
        MONKEYS.append(Monkey(monkey_def))

for m in MONKEYS:
    m.print()

if 1 == PART:
    nrounds = 20
elif 2 == PART:
    nrounds = 10000

for d in DIVISORS:
    COMMON = COMMON * d
    
for round in range(0,nrounds):            
    activities = []
    nitems = 0
    for m in MONKEYS:
        m.update()
        activities.append(m.activity)

    if 0 == round % 20:
        print('Round', round)
        # print('activities:', activities)
        # for m in MONKEYS:
        #     nitems = nitems + len(m.items)
        #print('N:', nitems)
    
m0 = max(activities)
activities.remove(m0)
m1 = max(activities)
print('Product of top 2 activities:', m0*m1)
