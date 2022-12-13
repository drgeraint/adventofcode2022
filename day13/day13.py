#! /usr/bin/env python3

from functools import cmp_to_key

#with open('test.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

def lt(L, R):
    #print('compare:', L, R)
    answer = None
    if type(L) is int and type(R) is int:
        if L < R:
            answer = True
        elif L > R:
            answer = False
    elif type(L) is int and type(R) is list:
        answer = lt([L], R)
    elif type(L) is list and type(R) is int:
        answer = lt(L, [R])
    else:
        i = 0
        nl = len(L)
        nr = len(R)
        while None is answer and i < min(nl, nr)+1:
            if nl <= i and nr <= i:
                answer = None
            elif nl <= i and nr > i:
                answer = True
            elif nl > i and nr <= i:
                answer = False
            else:
                answer = lt(L[i], R[i])
            i += 1
    return answer

D1 = [[2]]
D2 = [[6]]
PACKETS = [D1, D2]

n = len(lines)
count = 0
total = 0
for i in range(0, n, 3):
    count += 1
    L = eval(lines[i])
    R = eval(lines[i+1])
    if lt(L, R):
        total += count
        PACKETS.append(L)
        PACKETS.append(R)
    else:
        PACKETS.append(R)
        PACKETS.append(L)

print('Part 1:', total)
        
def cmp(L, R):
    if lt(L, R):
        return -1
    else:
        return 1

PACKETS.sort(key=cmp_to_key(cmp))

count = 1
for i in PACKETS:
    #print(i)
    if D1 is i:
        n1 = count
    elif D2 is i:
        n2 = count
    count += 1

print('Part 2:', n1*n2)
