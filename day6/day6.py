#! /usr/bin/env python3

import copy

#with open('test.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

for line in lines:
    s = set()
    i = 3
    while len(s) < 4:
        i = i + 1
        x = line[i-4:i];
        s = set(x)
    print('Part 1:', i)

    s = set()
    i = 13
    while len(s) < 14:
        i = i + 1
        x = line[i-14:i];
        s = set(x)
    print('Part 2:', i)

