#! /usr/bin/env python3

#with open('test.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

MAP = {}
XMIN = 1000000
XMAX = 0
YMIN = 1000000
YMAX = 0

for line in lines:
    words = line.split()
    for i in range(1, len(words), 2):
        p1 = eval('('+words[i-1]+')')
        p2 = eval('('+words[i+1]+')')
        #print(p1, p2)
        if p1[0] == p2[0]:      # horizontal
            x = p1[0]
            ymin = min([p1[1], p2[1]])
            ymax = max([p1[1], p2[1]])
            XMIN = min(XMIN, x)
            XMAX = max(XMAX, x)
            YMIN = min(YMIN, ymin)
            YMAX = max(YMAX, ymax)
            for y in range(ymin, ymax+1):
                MAP[(x, y)] = '#'
                #print(x,y, '#')
        elif p1[1] == p2[1]:    # vertical
            y = p1[1]
            xmin = min([p1[0], p2[0]])
            xmax = max([p1[0], p2[0]])
            XMIN = min(XMIN, xmin)
            XMAX = max(XMAX, xmax)
            YMIN = min(YMIN, y)
            for x in range(xmin, xmax+1):
                MAP[(x, y)] = '#'
                #print(x,y, '#')
        else:
            print('Warning: unexpected input')
                
        for x in range(p1[0], p2[0]+1):
            for y in range(p1[1], p2[1]+1):
                MAP[(x,y)] = '#'

def display_map():
    display = ''
    for y in range(0, YMAX+1):
        display += str(y)+' '
        for x in range(XMIN, XMAX+1):
            if (x,y) in MAP:
                display += MAP[(x,y)]
            else:
                display += ' '
        display += '\n'
    print(display)

SAND = []
abyss  = False
falling = False
while not abyss:
    if not falling:
        xsand = 500
        ysand = 0
        falling = True
    if ysand == YMAX:
        abyss = True
    else:
        if (xsand, ysand+1) not in MAP:
            ysand += 1
        elif (xsand-1, ysand+1) not in MAP:
            xsand -= 1
            ysand += 1
        elif (xsand+1, ysand+1) not in MAP:
            xsand += 1
            ysand += 1
        else:
            MAP[(xsand,ysand)] = 'o'
            SAND.append((xsand,ysand))
            falling = False
display_map()
print('Part 1:', len(SAND))
        
