#! /usr/bin/env python3

import pandas as pd

nsteps = 1000000000000
period = 1745

with open('results.csv', 'r') as fin:
    results = pd.read_csv(fin, delimiter=',')

cols = results.columns
for name in cols:
    results.rename(columns={name:name.strip(' "')}, inplace=True)
data = results['top'].diff()

def find_period(data):
    pmax = 0
    imax = 0
    lags = [x for x in range(1, 100)]
    for x in range(100, 10000, 5):
        lags.append(x)

    xmax = 0
    for i in lags:
        x = data.autocorr(i)
        if x > xmax:
            xmax   = x
            period = i
            print('Best correlation so far:', period, x)
    return period

if None is period:
    period = find_period(data)

def f(n):
    global data
    global period
    global results
    data0 = data[:period]
    data1 = data[2*period:3*period]
    if n < period:
        y = data0[:n+1].sum()
    else:
        a = int(n/period)-1
        b = int(n%period)
        y = data0.sum()+a*data1.sum()+data1[:b+1].sum()
    return int(y)

def check_f():
    for i in range(1, int(len(data)/period)):
        assert(data[i*period:(i+1)*period].sum() == data[2*period:3*period].sum())
        print('All periods after the first have the same sum')
        print('Checking all available results')
        for i in range(0, len(data)):
            assert(f(i) == results.top[i])
        print('OK')
    
print('Part 2:', f(nsteps))
