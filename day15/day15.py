#! /usr/bin/env python3

#filename   = 'test.txt'
filename   = 'input.txt'

PART       = 1

MAP        = {}
SENSORS    = []
BEACONS    = []
XMIN       = 0
XMAX       = 0
YMIN       = 0
YMAX       = 0
if 'test.txt' == filename:
    TARGET_ROW = 10
    MIN	       = 0
    MAX        = 20
elif 'input.txt' == filename:
    TARGET_ROW = 2000000
    MIN	       = 0
    MAX        = 4000000

def print_map(xmin=XMIN, xmax=XMAX, ymin=YMIN, ymax=YMAX):
    display = ''
    for y in range(ymin, ymax+1):
        display += str(y).zfill(4)+' '
        for x in range(xmin, xmax+1):
            if (x,y) in MAP:
                display += MAP[(x,y)]
            else:
                display += ' '
        display += '\n'
    print(display)
    
class Sensor:
    def __init__ (self, s, b):
        self.s = s
        self.sx = s[0]
        self.sy = s[1]
        self.b = b
        self.bx = b[0]
        self.by = b[1]
        self.d = abs(self.sx-self.bx)+abs(self.sy-self.by)
        SENSORS.append(self)
        BEACONS.append(b)
        MAP[s] = 'S'
        MAP[b] = 'B'
        global XMIN
        global XMAX
        global YMIN
        global YMAX
        XMIN = min(XMIN, self.sx-self.d-1)
        XMAX = max(XMAX, self.sx+self.d+1)
        YMIN = min(YMIN, self.sy-self.d-1)
        YMAX = max(YMAX, self.sy+self.d+1)
        ymin = self.sy - self.d
        ymax = self.sy + self.d
        # for y in range(ymin, ymax+1):  # Uses too much memory for large input
        if 1 == PART:
            if TARGET_ROW in range(self.sy-self.d, self.sy+self.d+1):
                yrange = [TARGET_ROW]
            else:
                yrange = []
            for y in yrange:
                xmin = max(XMIN, self.sx - abs(self.d - abs(self.sy-y)))
                xmax = min(XMAX, self.sx + abs(self.d - abs(self.sy-y)))
                for x in range(xmin, xmax+1):
                    if (x,y) not in MAP:
                        MAP[(x,y)] = '#'
        # elif 2 == PART:
        #     XMIN = MIN
        #     XMAX = MAX+1
        #     YMIN = MIN
        #     YMAX = MAX+1
        #     yrange = range(max(YMIN, self.sy-self.d), min(YMAX,self.sy+self.d+1))
       
with open(filename, 'r') as fin:
    lines = fin.read().splitlines()

for line in lines:
    words = line.split()
    sx = int(words[2].strip(',')[2:])
    sy = int(words[3].strip(':')[2:])
    bx = int(words[8].strip(',')[2:])
    by = int(words[9].strip(':')[2:])
    s  = (sx,sy)
    b  = (bx,by)
    Sensor(s,b)

#Sensor((2,18),(-2,15))
#Sensor((8,7),(2,10))
if 'test.txt' == filename:
    print_map(XMIN, XMAX, YMIN, YMAX)

if 1 == PART:
    count = 0
    y = TARGET_ROW
    for x in range(XMIN, XMAX+1):
        if (x,y) in MAP and '#' == MAP[(x,y)]:
            count += 1 
    print('Part 1:', count)
# elif 2 == PART:
#     for x in range(MIN, MAX+1):
#         for y in range(MIN, MAX+1):
#             if (x,y) not in MAP:
#                 print(x,y)
#                 print('Part 2:', x*4000000+y)
                

