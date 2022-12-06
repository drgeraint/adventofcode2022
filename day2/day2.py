#! /usr/bin/env python3

with open('input.txt', 'r') as fin:
    lines = fin.read().splitlines()

ROCK     = 1
PAPER    = 2
SCISSORS = 3

WIN      = 6
DRAW     = 3
LOSE     = 0

SCORE1 = {                      # (opponent, me) : me + result
    (ROCK, ROCK)         : ROCK     + DRAW,
    (ROCK, PAPER)        : PAPER    + WIN,
    (ROCK, SCISSORS)     : SCISSORS + LOSE,
    (PAPER, ROCK)        : ROCK     + LOSE,
    (PAPER, PAPER)       : PAPER    + DRAW,
    (PAPER, SCISSORS)    : SCISSORS + WIN,
    (SCISSORS, ROCK)     : ROCK     + WIN,
    (SCISSORS, PAPER)    : PAPER    + LOSE,
    (SCISSORS, SCISSORS) : SCISSORS + DRAW }

MAP1 = {                        
    'A' : ROCK, 'B' : PAPER, 'C' : SCISSORS,
    'X' : ROCK, 'Y' : PAPER, 'Z' : SCISSORS }

total = 0
for line in lines:
    marks = SCORE1[(MAP1[line[0]], MAP1[line[2]])]
    total = total + marks

print('Part 1:', total)

MAP2 = {
    'A' : ROCK, 'B' : PAPER, 'C' : SCISSORS,
    'X' : LOSE, 'Y' : DRAW,  'Z' : WIN }

SCORE2 = {                      # (opponent, result) : me + result
    (ROCK, LOSE)     : SCISSORS + LOSE,
    (ROCK, DRAW)     : ROCK     + DRAW,
    (ROCK, WIN)      : PAPER    + WIN,
    (PAPER, LOSE)    : ROCK     + LOSE,
    (PAPER, DRAW)    : PAPER    + DRAW,
    (PAPER, WIN)     : SCISSORS + WIN,
    (SCISSORS, LOSE) : PAPER    + LOSE,
    (SCISSORS, DRAW) : SCISSORS + DRAW,
    (SCISSORS, WIN)  : ROCK     + WIN }

total = 0
for line in lines:
    marks = SCORE2[(MAP2[line[0]], MAP2[line[2]])]
    total = total + marks

print('Part 2:', total)

    
