#! /usr/bin/env python3

TOP    = 0
MAP    = {}
SHAPES = []
SEQ = { 'Minus' : 'Plus()', 'Plus' : 'L()', 'L' : 'I()', 'I' : 'O()', 'O' : 'Minus()' }

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, coord):
        x = self.x + coord.x
        y = self.y + coord.y
        return Coord(x,y)
        
    def down(self):        
        return Coord(self.x, self.y-1)

    def left(self):
        return Coord(self.x-1, self.y)
        
    def right(self):
        return Coord(self.x+1, self.y)

    def pos(self):
        return (self.x, self.y)
    
class Shape:
    def __init__(self, kind):
        global TOP
        self.init   = Coord(2, TOP + 4)
        self.points = []
        self.kind   = kind
        SHAPES.append(self)
        
    def down(self):
        global MAP
        global TOP        
        new_points = [point.down() for point in self.points]
        if self.move(new_points):
            self.points = new_points
        else:
            for point in self.points:
                MAP[(point.x, point.y)] = '#'
                if point.y > TOP:
                    TOP = point.y
            if len(SHAPES) < 2022:        
                eval(SEQ[self.kind]) # New Shape
                
    def left(self):
        new_points = [point.left() for point in self.points]
        if self.move(new_points):
            self.points = new_points
        
    def right(self):
        new_points = [point.right() for point in self.points]
        if self.move(new_points):
            self.points = new_points
            
    def move(self, new_points):
        move = True
        for point in new_points:
            if point.x < 0 or point.x > 6 or (point.x, point.y) in MAP or point.y < 0:
                move = False
        return move

    def pos(self):
        return ([point.pos() for point in self.points])
    
class Minus(Shape):
    def __init__(self):
        Shape.__init__(self, 'Minus')
        points = [Coord(0,0), Coord(1,0), Coord(2,0), Coord(3,0)]
        self.points = [point+self.init for point in points]
        
class Plus(Shape):
    def __init__(self):
        Shape.__init__(self, 'Plus')
        points = [Coord(1,0), Coord(0,1), Coord(1,1), Coord(2,1), Coord(1,2)]
        self.points = [point+self.init for point in points]
        
class L(Shape):
    def __init__(self):
        Shape.__init__(self, 'L')
        points = [Coord(0,0), Coord(1,0), Coord(2,0), Coord(2,1), Coord(2,2)]
        self.points = [point+self.init for point in points]
        
class I(Shape):
    def __init__(self):
        Shape.__init__(self, 'I')
        points = [Coord(0,0), Coord(0,1), Coord(0,2), Coord(0,3)]
        self.points = [point+self.init for point in points]
        
class O(Shape):
    def __init__(self):
        Shape.__init__(self, 'O')
        points = [Coord(0,0), Coord(1,0), Coord(0,1), Coord(1,1)]
        self.points = [point+self.init for point in points]
        
def down():
    shape = SHAPES[-1]
    shape.down()

def left():
    shape = SHAPES[-1]
    shape.down()
    shape = SHAPES[-1]
    shape.left()
    
def right():
    shape = SHAPES[-1]
    shape.down()
    shape = SHAPES[-1]
    shape.right()

def print_map():
    s = ''
    for y in range(TOP, -1, -1):
        s += str(y).zfill(4)+' '
        for x in range(0, 7):
            p = (x,y)
            if p in MAP:
                s += MAP[p]
            else:
                s += '.'
        s += '\n'
    print(s)
                
start = 'Minus'
eval(start+'()')

#with open('test.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    line = fin.read()

    
while len(SHAPES) < 2022:
    for c in line:
        if '<' is c:
            left()
        elif '>' is c:
            right()

print_map()
print('nshapes:', len(SHAPES))
print('Part 1:', TOP+1)
