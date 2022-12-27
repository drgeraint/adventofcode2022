#! /usr/bin/env python3

import sys
sys.setrecursionlimit(10000)

PART = 2

#filename = 'test.txt'
filename = 'input.txt'

if 1 == PART:
    TIME = 30
elif 2 == PART:
    TIME = 26
        
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
    return val

def elephant(path):
    target = TARGET.copy()
    for tag in path:
        if tag in target:
            target.remove(tag)
    dp = 0
    paths = VALVES[START].find_paths([], target)
    elephant_path = None
    for p in paths:
        x = evaluate(p)
        if x > dp:
            dp    = x
            elephant_path = p
    return (dp, elephant_path)

def evaluate(path):
    dp = 0
    if path:
        t = TIME
        i = 0
        while i < len(path) and 1 < t:
            tag = path[i]
            if path == BEST['path']:
                print('t:', TIME+1-t, tag)
            v = VALVES[tag]
            q = v.flow
            if q > 0:
                t  -= 1
                dp += max(0,t)*q
                if path == BEST['path']:
                    print('t:', TIME+1-t, tag, dp)
            i += 1        
            if i < len(path):
                nxt = path[i]
                dt = v.steps[nxt]
                t -= v.steps[nxt]
    return dp

def evaluate2(path):
    dp = evaluate(path)
    x  = elephant(path)
    elephant_dp   = x[0]
    elephant_path = x[1]
    dp += elephant_dp
    return (dp, elephant_path)
            
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
                    changed = True
                elif self.steps[c] > v.steps[c]+1:
                    old = self.steps[c]
                    new = v.steps[c] + 1
                    self.steps[c] = new
                    changed = True
        return changed

    # Need to update to find for elephant reduced target also
    def find_paths(self, path=[], target=TARGET):
        global BEST
        if self.name not in path:
            path.append(self.name)
        x = distance(path)
        if x <= TIME and len(path) <= len(target):
            paths = []
            for c in target:
                if c not in path:
                    v = VALVES[c]
                    new_paths = v.find_paths(path.copy(), target)
                    for p in new_paths:
                        paths.append(p.copy())
                        if 1 == PART and target is TARGET:
                            score = evaluate(p)
                            if score > BEST['score']:
                                print('New best:', score, p)
                                BEST['score'] = score
                                BEST['path' ] = p
                        elif 2 == PART and target is TARGET:
                            x = evaluate2(p)
                            score = x[0]
                            elephant_path = x[1]
                            if score > BEST['score']:
                                print('New best:', score, p)
                                BEST['score'] = score
                                BEST['path' ] = p
                                BEST['elephant_path'] = elephant_path
                                print(BEST)
                        elif 2 == PART and target is not TARGET:
                            score = evaluate(p)
        else:
                if 1 == PART and target is TARGET:
                    score = evaluate(path)
                    if score > BEST['score']:
                        print('New best:', score, path)
                        BEST['score'] = score
                        BEST['path' ] = path
                elif 2 == PART and target is TARGET:
                    x = evaluate2(path)
                    score = x[0]
                    elephant_path = x[1]
                    if score > BEST['score']:
                        print('New best:', score, path)
                        BEST['score'] = score
                        BEST['path' ] = path
                        BEST['elephant_path'] = elephant_path
                        print(BEST)
                elif 2 == PART and target is not TARGET:
                    score = evaluate(path)
                paths = [path]
                
        return paths
                
for line in lines:
    words = line.split()
    if START is None:
       START = words[1]
    Valve(words[1], int(words[4][5:].strip(';')), [c.strip(',') for c in words[9:]])

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

if 'test.txt' == filename:
    print(VALVES[START].steps)

if 'test.txt' == filename:
    for tag in VALVES:
        print(VALVES[tag].steps)

paths = VALVES[START].find_paths([], TARGET)

for p in paths:
    path = (START,)+p
    if 1 == PART:
        x = evaluate(path)
    elif 2 == PART:
        x = evaluate2(path)
    if x > BEST['score']:
        BEST['score'] = x
        BEST['path']  = path
        print('New best:', x, path)

print('TARGET', TARGET)

if 1 == PART:
    print('Part 1', BEST['score'], BEST['path'])
    evaluate(BEST['path'])
elif 2 == PART:
    print('Part 2', BEST)
    evaluate(BEST['path'])
    evaluate(BEST['elephant_path'])
