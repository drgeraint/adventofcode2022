#! /usr/bin/env python3

PART   = 2

MAP    = {}
SAND   = []
SOURCE = (500,0)
YMAX   = 0

#with open('test.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

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
            YMAX = max(YMAX, ymax)
            for y in range(ymin, ymax+1):
                MAP[(x, y)] = '#'
                #print(x,y, '#')
        elif p1[1] == p2[1]:    # vertical
            y = p1[1]
            xmin = min([p1[0], p2[0]])
            xmax = max([p1[0], p2[0]])
            YMAX = max(YMAX, y)
            for x in range(xmin, xmax+1):
                MAP[(x, y)] = '#'
                #print(x,y, '#')
        else:
            print('Warning: unexpected input')

def xrange():
    return range(SOURCE[0]-YMAX, SOURCE[0]+YMAX+1)
            
if 2 == PART:
    YMAX += 2
    for x in xrange():
        MAP[(x, YMAX)] = '#'
            
def display_map():
    display = ''
    for y in range(0, YMAX+1):
        display += str(y)+' '
        for x in xrange():
            if (x,y) in MAP:
                display += MAP[(x,y)]
            else:
                display += ' '
        display += '\n'
    print(display)
    
abyss   = False
blocked = False
falling = False

while not abyss and not blocked:
    if not falling:
        xsand = SOURCE[0]
        ysand = SOURCE[1]
        falling = True
    if SOURCE in MAP:
        blocked = True
    elif ysand == YMAX:
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
print('Part', PART, ':', len(SAND))

