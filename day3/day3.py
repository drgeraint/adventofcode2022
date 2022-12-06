#! /usr/bin/env python3

with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

MAP = {}
for i in range(ord('a'),ord('z')+1):
    MAP[chr(i)] = i-ord('a')+1
for i in range(ord('A'),ord('Z')+1):
    MAP[chr(i)] = i-ord('A')+27
    
total1 = 0
for line in lines:
    n = len(line)
    x = int(n/2)
    line1 = line[:x]
    line2 = line[x:]
    common = list(set(line1) & set(line2))
    if len(common) > 0:
        priority = MAP[common[0]]
        total1 = total1 + priority
        
print('Part 1:', total1)

total2 = 0
for i in range(0, int(len(lines)/3)):
    line0 = lines[3*i]
    line1 = lines[3*i+1]
    line2 = lines[3*i+2]
    common = list(set(line0) & set(line1) & set(line2))
    priority = MAP[common[0]]
    total2 = total2 + priority

print('Part 2:', total2)
