#! /usr/bin/env python3

HEAD = [0,0]
TAIL_TRAIL = set()

part = 2
if 1 == part:
        n = 2
elif 2 == part:
        n = 10

KNOTS = [HEAD]
for i in range(0,n-1):
        KNOTS.append([0,0])

def update_tail():
        global KNOTS
        global TAIL_TRAIL
        for i in range(1,n):
                head = KNOTS[i-1]
                tail = KNOTS[i]                
                if abs(head[0]-tail[0]) > 1 or abs(head[1]-tail[1]) > 1:
                        if head[0] > tail[0]:
                                tail[0] = tail[0] + 1
                        elif head[0] < tail[0]:
                                tail[0] = tail[0] - 1
                        if head[1] > tail[1]:
                                tail[1] = tail[1] + 1
                        elif head[1] < tail[1]:
                                tail[1] = tail[1] - 1
                TAIL_TRAIL.add(tuple(KNOTS[-1]))
                                
def R():
        HEAD[0] = HEAD[0] + 1
        update_tail()

def L():
        global HEAD
        HEAD[0] = HEAD[0] - 1
        update_tail()

def U():
        global HEAD
        HEAD[1] = HEAD[1] + 1
        update_tail()

def D():
        global HEAD
        HEAD[1] = HEAD[1] - 1
        update_tail()

#with open('test.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
	lines = fin.read().splitlines()

for line in lines:
        words = line.split()
        direction = words[0]
        assert(direction in ('R', 'L', 'U', 'D'))
        distance  = int(words[1])
        for i in range(0, distance):
                eval(direction+'()')

print(len(TAIL_TRAIL))
