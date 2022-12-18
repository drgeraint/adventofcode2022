#! /usr/bin/env python3

#with open('test.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

CUBES = {}

class Cube:
    def __init__(self, pos):
        self.pos = pos
        CUBES[(pos)] = self

    def neighbours(self):
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
        for pos in adjacent:
            if pos is not self.pos:
                if pos in CUBES:
                    count += 1
        return count

    def exposed(self):
        val = 6 - self.neighbours()
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
