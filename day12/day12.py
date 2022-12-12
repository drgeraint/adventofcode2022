#! /usr/bin/env python3

import sys
sys.setrecursionlimit(100000)

with open('input.txt', 'r') as fin:
#with open('test.txt', 'r') as fin:
    lines = fin.read().splitlines()

MAP = {}
A   = []

ZMIN = ord('a')
ZMAX = ord('z')+1

row = 0
for line in lines:
    col = 0
    for c in line:
        MAP[(row,col)] = ord(c)
        if 'S' == c:
            START = (row,col)
            MAP[(row,col)] = ZMIN
        elif 'E' == c:
            END = (row,col)
            MAP[(row,col)] = ZMAX
        elif 'a' == c:
            A.append((row,col))
        col += 1
    row += 1
    
#print(map)

STEPS = {}
NODES = {}

class Node:
    def __init__(self, pos, z, k):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.z = z
        self.k = k
        STEPS[pos] = k
        NODES[pos] = self

    def explore(self):
        for pos in [(self.x+1,self.y), (self.x,self.y+1), (self.x-1,self.y), (self.x,self.y-1)]:
            if pos in MAP:
                #print('Found position', pos)
                if MAP[pos] <= self.z + 1:
                    #print('Position', pos, 'is reachable')
                    if pos in STEPS:
                        #print('Position', pos, 'has been found before')
                        if STEPS[pos] <= self.k + 1:
                            pass
                        else:
                            #print('Position', pos, 'is closer than previously discovered')
                            NODES[pos].update(self.k + 1)
                    else:
                        #print('Position', pos, 'is a new node')
                        n = Node(pos, MAP[pos], self.k + 1)
                        n.explore()

    def update(self, k):
        self.k = k
        STEPS[self.pos] = k
        self.explore()
                        
S = Node(START, ord('a'), 0)
S.explore()

print('Part 1:', STEPS[END])

for n in A:
    NODES[n].update(0)

print('Part 2:', STEPS[END])
