#! /usr/bin/env python3
import sys

if len(sys.argv) > 1:
    infile = sys.argv[1]
else:
    infile = 'test.txt'

if len(sys.argv) > 2:
    outfile = sys.argv[2]
else:
    outfile = 'nodes.dot'

with open(infile, 'r') as fin:
    lines = fin.read().splitlines()

graph = {}
flows = {}
for line in lines:
    words = line.split()
    node0 = words[1]
    nodes = [w.strip(',') for w in words[9:]]    
    graph[node0] = nodes
    flow  = words[4][5:].strip(';')
    flows[node0] = flow
print(graph)

text = ['digraph G {',
        ' Node [style="rounded,filled", shape=egg]']
for node in graph:
    style = ''
    if 'AA' == node:
        style += 'color=red, '
    if 0 < int(flows[node]):
        style += 'fillcolor=yellow'
    else:
        style += 'fillcolor=white'
    text.append(' '+node+' [label="'+node+'\n'+flows[node]+'",'+style+']')

for node in graph:
    for edge in graph[node]:
        text.append(' '+node+' -> '+edge+';')

text.append('}')
        
with open(outfile, 'x') as fout:
    fout.writelines("%s\n" % s for s in text)
    
