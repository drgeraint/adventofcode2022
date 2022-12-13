#! /usr/bin/env python3

#with open('test.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

def lt(L, R):
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
        try:
            if L < R:
                answer = True
            elif L > R:
                answer = False
        except TypeError as e:
            s = str(e).split()
            if "'int'" == s[6] and "'list'" == s[8]:
                L = [L]
            elif "'list'" == s[8] and "'int'" == s[8]:
                R = [R]
            i = 0
            while None is answer:
                nl = len(L)
                nr = len(R)
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
        
n = len(lines)
count = 0
total = 0
for i in range(0, n, 3):
    count += 1
    L = eval(lines[i])
    R = eval(lines[i+1])
    if lt(L, R):
        total += count

print(total)
