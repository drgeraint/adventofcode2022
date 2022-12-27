#! /usr/bin/env python3

PART = 2

#puzzle = 'test'
puzzle = 'input'

with open(puzzle+'.txt', 'r') as fin:
    lines = fin.read().splitlines()

NODES = []

HEAD = None

class Node:
    def __init__(self, val):
        global HEAD
        i = len(NODES)
        NODES.append(self)
        self.val  = int(val)
        if 2 == PART:
            self.val *= 811589153
        self.tail = None
        if 0 == i:
            HEAD = self
            self.head  = None
        else:
            self.start = False
            self.head  = NODES[i-1]
            self.head.tail = self
            
    def move_up(self):        
        global HEAD
        old_head = self.head
        old_tail = self.tail
        new_head = old_head.head
        new_tail = old_head
        old_tail.head = new_tail
        old_head.tail = old_tail
        self.head = new_head
        self.tail = new_tail
        new_head.tail = self
        new_tail.head = self
        
    def move_down(self):
        global HEAD
        old_head = self.head
        old_tail = self.tail
        new_head = old_tail
        new_tail = old_tail.tail
        if HEAD is self:
            HEAD = old_tail
        old_head.tail = old_tail
        old_tail.head = old_head
        self.head = new_head
        self.tail = new_tail
        new_head.tail = self
        new_tail.head = self
        
    def move(self):
        if self.val > 0:
            for i in range(0, self.val % (len(NODES)-1)):
                self.move_down()
        elif self.val < 0:
            for i in range(0, -self.val % (len(NODES)-1)):
                self.move_up()
            
for line in lines:
    Node(line)

# link ends
NODES[ 0].head = NODES[-1]
NODES[-1].tail = NODES[ 0]

def print_nodes():
    global HEAD
    n = HEAD
    l = [n.val]
    for i in range(1, len(NODES)):
        n = n.tail
        l.append(n.val)
    print(l)
    
if 'test' == puzzle:
    print([n.val for n in NODES])
if 1 is PART:
    reps = 1
elif 2 is PART:
    reps = 10
for i in range(0, reps):
    for n in NODES:
        n.move()
    if 'test' == puzzle:
        print_nodes()
    n = HEAD
    while 0 is not n.val:
        n = n.tail    
    HEAD = n

N = 1000

if 'test' == puzzle:
    print_nodes()

ans = []
for i in range(1, 3*N+1):
    n = n.tail
    if 0 == i % N:
        print(i, i % N, n.val)
        ans.append(n.val)

print(ans)
print('Part', PART, ':',  sum(ans))
