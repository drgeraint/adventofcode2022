#! /usr/bin/env python3

#filename = 'test.txt'
filename = 'input.txt'

with open(filename, 'r') as fin:
    lines = fin.read().splitlines()

BEST   = { 'score': 0, 'path': None }
START  = 'AA'
TARGET = []
VALVES = {}

def distance(path):
    val = 0
    tag = path[0]
    v   = VALVES[tag]
    for i in range(1, len(path)):
        nxt = path[i]
        val += v.steps[nxt]
        v = VALVES[nxt]
    if 'test.txt' == filename:
        print('distance:', val, path)
    return val

def evaluate(path):
    dp = 0
    t  = 30
    i = 0
    while i < len(path) and 1 < t:
        tag = path[i]
        if path == BEST['path']:
            print('t:', 31-t, tag)
        v = VALVES[tag]
        q = v.flow
        if q > 0:
            t  -= 1
            dp += max(0,t)*q
            if path == BEST['path']:
                print('t:', 31-t, tag, dp)
        i += 1        
        if i < len(path):
            nxt = path[i]
            dt = v.steps[nxt]
            t -= v.steps[nxt]
    return dp
        
class Valve:
    def __init__(self, tag, flow, cnxn):
        self.name = tag
        self.flow = flow
        self.cnxn = cnxn
        VALVES[tag] = self
        if 0 < flow:
            TARGET.append(tag)
        self.steps = {tag: 0}
        for c in self.cnxn:
            self.steps[c] = 1
        
    def update(self):
        changed = False
        for tag in self.cnxn:
            v = VALVES[tag]
            for c in v.steps:
                if c not in self.steps:
                    self.steps[c] = v.steps[c] + 1
                    print('Added', tag, '->', c, '=', self.steps[c])
                    changed = True
                elif self.steps[c] > v.steps[c]+1:
                    old = self.steps[c]
                    new = v.steps[c] + 1
                    self.steps[c] = new
                    print('Updated', tag, '->', c, 'from', old, 'to', new)
                    changed = True
        return changed
                    
    def find_paths(self, path=[]):
        global BEST
        if self.name not in path:
            path.append(self.name)
        x = distance(path)
        if x <= 30 and len(path) <= len(TARGET):
            paths = []
            for c in TARGET:
                if c not in path:
                    v = VALVES[c]
                    new_paths = v.find_paths(path.copy())
                    for p in new_paths:
                        paths.append(p.copy())
                        score = evaluate(p)
                        if score > BEST['score']:
                            print('New best:', score, p)
                            BEST['score'] = score
                            BEST['path' ] = p
        else:
            score = evaluate(path)
            if score > BEST['score']:
                print('New best:', score, path)
                BEST['score'] = score
                BEST['path' ] = path
            paths = []
        return paths
                
for line in lines:
    words = line.split()
    if START is None:
       START = words[1]
    Valve(words[1], int(words[4][5:].strip(';')), [c.strip(',') for c in words[9:]])
print('Valves created')

i = 0
do_update = True
while do_update:
    if i > len(VALVES):
        do_update = False
    for tag in VALVES:
        v = VALVES[tag]
        changed = v.update()
        if changed:
            do_update = True
    i += 1
print('Intervalve distances updated:', i)

if 'test.txt' == filename:
    print(VALVES[START].steps)

if 'test.txt' == filename:
    for tag in VALVES:
        print(VALVES[tag].steps)

paths = VALVES[START].find_paths()

for p in paths:
    path = (START,)+p
    x = evaluate(path)
    if x > BEST['score']:
        BEST['score'] = x
        BEST['path']  = path
        print('New best:', x, path)

print('Part 1', BEST['score'], BEST['path'])
print('TARGET', TARGET)
evaluate(BEST['path'])
