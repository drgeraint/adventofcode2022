#! /usr/bin/env python3

import sys
sys.setrecursionlimit(100000)

with open('input.txt', 'r') as fin:
#with open('test.txt', 'r') as fin:
    lines = fin.read().splitlines()

MAP   = {}                      # Map of elevations read from input
ALIST = []                      # List of nodes with elevation 'a' (for Part 2)

zmin = ord('a')                 # Numeric elevation of lowest elevation
zmax = ord('z')+1               # Numeric elevation of highest elevation

row = 0
for line in lines:
    col = 0
    for c in line:
        MAP[(row,col)] = ord(c) # Numeric elevation of position
        if 'S' == c:
            START = (row,col)
            MAP[(row,col)] = zmin
        elif 'E' == c:
            END = (row,col)
            MAP[(row,col)] = zmax
        elif 'a' == c:
            ALIST.append((row,col)) # For part 2, instead of searching for elevation ord('a') later
        col += 1
    row += 1
    
STEPS = {}                      # Steps to reach each node. For convenience, could use NODES[pos].k instead.
NODES = {}                      # All nodes that have been reached from START

class Node:
    def __init__(self, pos, z, k):
        self.pos = pos          # (row,col)
        self.z = z              # elevation
        self.k = k              # steps from START
        STEPS[pos] = k
        NODES[pos] = self

    def explore(self):
        x = self.pos[0]
        y = self.pos[1]
        next_step = self.k + 1
        for pos in [(x+1,y), (x,y+1), (x-1,y), (x,y-1)]:
            if pos in MAP:
                #print('Found position', pos)
                if MAP[pos] <= self.z + 1:
                    #print('Position', pos, 'is reachable')
                    if pos in STEPS:
                        #print('Position', pos, 'has been found before')
                        if STEPS[pos] <= next_step:
                            pass
                        else:
                            #print('Position', pos, 'is closer than previously discovered')
                            NODES[pos].update(next_step)
                    else:
                        #print('Position', pos, 'is a new node')
                        n = Node(pos, MAP[pos], next_step)
                        n.explore()

    def update(self, k):
        self.k = k
        STEPS[self.pos] = k
        self.explore()          # Update steps (k) for adjacent nodes
                        
S = Node(START, ord('a'), 0)
S.explore()

print('Part 1:', STEPS[END])

for n in ALIST:
    NODES[n].update(0)

print('Part 2:', STEPS[END])
