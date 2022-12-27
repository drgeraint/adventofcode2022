#! /usr/bin/env python3

PART = 2

import sys
sys.setrecursionlimit(100000)

#with open('test.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

CUBES = {}
STEAM = {}
AIR   = {}

class Cube:
    def __init__(self, pos):
        self.pos = pos
        CUBES[(pos)] = self

    def adjacent(self):
        count = 0
        x = self.pos[0]
        y = self.pos[1]
        z = self.pos[2]
        adjacent = [(x-1, y, z),
                    (x+1, y, z),
                    (x, y-1, z),
                    (x, y+1, z),
                    (x, y, z-1),
                    (x, y, z+1)]
        return adjacent

    def exposed(self):
        adjacent = 0
        for pos in self.adjacent():
            if pos is not self.pos:
                if pos in CUBES:
                    adjacent += 1
                if 2 == PART:
                    if pos in AIR:
                        adjacent += 1

        val = 6 - adjacent
        #print('exposed:', pos, val)
        return val
        
for line in lines:
    words = line.split(',')
    pos = (int(words[0]), int(words[1]), int(words[2]))
    Cube(pos)
    
exposed = 0
for pos in CUBES:
    exposed += CUBES[pos].exposed()

print('Part 1:', exposed)

XMIN = None
YMIN = None
ZMIN = None

XMAX = None
YMAX = None
ZMAX = None

for pos in CUBES:
    x = pos[0]
    y = pos[1]
    z = pos[2]

    if XMIN is None or x < XMIN:
        XMIN = x
    if YMIN is None or y < YMIN:
        YMIN = y
    if ZMIN is None or z < ZMIN:
        ZMIN = z
        
    if XMAX is None or x > XMAX:
        XMAX = x
    if YMAX is None or y > YMAX:
        YMAX = y
    if ZMAX is None or z > ZMAX:
        ZMAX = z

def inbounds(pos):
    global XMIN, XMAX, YMIN, YMAX, ZMIN, ZMAX

    x = pos[0]
    y = pos[1]
    z = pos[2]

    val = False
    if XMIN <= x and x <= XMAX:
        if YMIN <= y and y <= YMAX:
            if ZMIN <= z and z <= ZMAX:
                val = True
    return val
    
class Steam(Cube):
    def __init__(self, pos):
        self.pos = pos
        STEAM[(pos)] = self
        self.propagate()
                
    def propagate(self):
        for pos in self.adjacent():
            if inbounds(pos):
                if pos not in STEAM and pos not in CUBES:
                    Steam(pos)

for x in [XMIN-1, XMAX+1]:
    for y in range(YMIN, YMAX+1):
        for z in range(ZMIN, ZMAX+1):
            pos = (x, y, z)
            if pos not in STEAM and pos not in CUBES:
                Steam(pos)
for y in [YMIN-1, YMAX+1]:
    for x in range(XMIN, XMAX+1):
        for z in range(ZMIN, ZMAX+1):
            pos = (x, y, x)
            if pos not in STEAM and pos not in CUBES:
                Steam(pos)
for z in [ZMIN-1, ZMAX+1]:
    for x in range(XMIN, XMAX+1):
        for y in range(YMIN, YMAX+1):
            pos = (x, y, z)
            if pos not in STEAM and pos not in CUBES:
                Steam(pos)

propagating = True
while propagating:
    nsteam = len(STEAM)
    for pos, s in STEAM.items():
        s.propagate()
    if len(STEAM) == nsteam:
        propagating = False
                

#print([x for x in CUBES])
#print([x for x in STEAM])

class Air(Cube):
    def __init__(self, pos):
        self.pos = pos
        AIR[(pos)] = self

    def propagate(self, pos):
        for pos in self.adjacent():
            if inbounds(pos):
                if pos not in STEAM and pos not in CUBES:
                    Air(pos)
                    print('Air propagated:', self.pos, pos)

for x in range(XMIN, XMAX+1):
    for y in range(YMIN, YMAX+1):
        for z in range(ZMIN, ZMAX+1):
            pos = (x, y, z)
            if pos not in STEAM and pos not in CUBES:
                Air(pos)


exposed2 = 0
for pos in CUBES:
    exposed2 += CUBES[pos].exposed()


print('Part 2:', exposed2)
#print(AIR)
