#! /usr/bin/env python3

HEAD = [0,0]
TAIL = [0,0]
#TAIL_TRAIL = set(tuple(TAIL))
TAIL_TRAIL = set()

KNOTS = [HEAD]
for i in range(0,9):
        KNOTS.append([0,0])

## Part 1
# def update_tail():
#         global TAIL
#         global TAIL_TRAIL
#         if abs(HEAD[0]-TAIL[0]) > 1 or abs(HEAD[1]-TAIL[1]) > 1:
#                 if HEAD[0] > TAIL[0]:
#                         TAIL[0] = TAIL[0] + 1
#                 elif HEAD[0] < TAIL[0]:
#                         TAIL[0] = TAIL[0] - 1
#                 if HEAD[1] > TAIL[1]:
#                         TAIL[1] = TAIL[1] + 1
#                 elif HEAD[1] < TAIL[1]:
#                         TAIL[1] = TAIL[1] - 1
#         TAIL_TRAIL.add(tuple(TAIL))

## Part 2
def update_tail():
        global KNOTS
        global TAIL_TRAIL
        for i in range(1,10):
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
                
def update_knots():
        global KNOTS
                
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
        direction = words[0]+'()'
        distance  = int(words[1])
        for i in range(0, distance):
                eval(direction)

print(len(TAIL_TRAIL))
