#! /usr/bin/env python3

with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

total1 = 0
total2 = 0
for line in lines:
    pair = line.split(',')
    x0 = pair[0].split('-')
    x1 = pair[1].split('-')
    r0 = set(range(int(x0[0]), int(x0[1])+1))
    r1 = set(range(int(x1[0]), int(x1[1])+1))
    if r0.issubset(r1) or r1.issubset(r0):
        total1 = total1 + 1
    common = r0 & r1
    if len(common) > 0:
        total2 = total2 + 1
print('Part 1:', total1)
print('Part 2:', total2)

