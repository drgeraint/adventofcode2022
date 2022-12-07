#! /usr/bin/env python3

DIRECTORIES = set()

class File:
    def __init__ (self, name, size):
        self.name = name
        self._size = int(size)

    def print(self):
        print(self.name, self._size)
        
    def size (self):
        return self._size

class Directory:
    def __init__(self, name):
        DIRECTORIES.add(self)
        self.name = name
        self.files = set()
        self.directories = {}

    def size(self):
        total = 0
        for f in self.files:
            total = total + f.size()
        for k, d in self.directories.items():
            total = total + d.size()
        return total
            
    def add_file(self, name, size):
        f = File(name, size)
        self.files.add(f)
        return f

    def add_directory(self, name):
        if name not in self.directories:
            d = Directory(name)
            d.parent = self
            self.directories[name] = d
        return self.directories[name]

    def print(self):
        print(self.name, self.size())

    def ls(self):
        for k, d in self.directories.items():
            d.print()
        for f in self.files:
            f.print()
        
ROOT = Directory('/')
PWD  = None

def cd(name):
    global PWD
    if name is '/':
        PWD = ROOT
    elif '..' == name:
        PWD = PWD.parent
    else:
        PWD = PWD.directories[name]
    # print('PWD =', PWD.name)

def check():
    cd('/')
    PWD.add_directory('a')
    PWD.add_file('b', 10)
    PWD.add_file('c', 20)
    PWD.add_directory('d')
    cd('d')
    PWD.add_file('e', 30)
    PWD.add_file('f', 40)
    cd('..')
    PWD.add_file('f', 50)
    
    for d in DIRECTORIES:
        d.print()

    assert(  0 == ROOT.directories['a'].size())
    assert( 70 == ROOT.directories['d'].size())
    assert(150 == ROOT.size())
    exit()

# check()
    
#with open('test.txt', 'r') as fin:
with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

for line in lines:
    words = line.split()
    if words[0] is '$':         # command
        command = words[1].strip()
        if 'cd' == command:
            dirname = words[2]
            cd(dirname)
        elif 'ls' == command:
            pass
        else:
            print('WARNING: Unexpected command #', command, '#')
    elif words[0].isnumeric(): # file
        filesize = words[0]
        filename = words[1]
        PWD.add_file(filename, filesize)
    elif 'dir' == words[0]:
        dirname = words[1]
        PWD.add_directory(dirname)
    else:
        print('WARNING: Unexpected output', line)

for d in DIRECTORIES:
    d.print()

total = 0
small_directories = set()
for d in DIRECTORIES:
    s = d.size()
    if 100000 > s:
        small_directories.add(d)
        total = total + s

print(small_directories)
print('Part 1:', total)

required  = 30000000
available = 70000000 - ROOT.size()
need_free = required - available

freed_space = 0
target = None
for d in DIRECTORIES:
    s = d.size()
    if s >= need_free:
        if freed_space < need_free or s < freed_space:
            target = d.name
            freed_space = s
            
print('Part 2:', target, freed_space)


