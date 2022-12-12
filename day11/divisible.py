#! /usr/bin/env python3

# Rules 3, 4, 7, 8, 9, 11, 13
# https://www.johndcook.com/blog/2020/11/10/test-for-divisibility-by-13/

# Rules 17, 19, 23
# https://divisible.info/DivisibilityRules/Divisibility-rule-for-17.html
# https://divisible.info/DivisibilityRules/Divisibility-rule-for-19.html
# https://divisible.info/DivisibilityRules/Divisibility-rule-for-23.html

table = {}
for d in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23):
    for n in range(0, 100000):
        table[(n,d)] = 0 == n % d

def divisible(n, d):
    if (n,d) in table:
        return table[(n,d)]
    elif type(n) == int and 1000 > n:
        if 0 > n:
            answer = divisible(-n, d)
        else:
            answer = n in table[d]
    elif type(n) == str and 7 > len(n):
        answer = divisible(int(n), d)
    else:
        s = str(n)
        if 0 == d:
            answer = False
        if 1 == d:
            answer = True
        if 2 == d:
            answer = s[-1] in ('0', '2', '4', '6', '8')
        elif 3 == d or 9 == d:
            sum = 0
            for i in s:
                sum = sum + int(i)
            answer = divisible(sum, d)
        elif 4 == d:
            # https://www.johndcook.com/blog/2020/11/10/test-for-divisibility-by-13/
            answer = divisible(int(s[-2:]), 4)
        elif 5 == d:
            answer = s[-1] in ('0', '5')
        elif 6 == d:
            answer = divisible(n, 2) and divisible(n, 3)
        elif 7 == d or 11 == d or 13 == d:
            # https://www.johndcook.com/blog/2020/11/10/test-for-divisibility-by-13/
            while not divisible(len(s), 3):
                s = '0'+s
            parts = [s[i*3:i*3+3] for i in range(0, int(len(s)/3))]
            sum = 0
            nparts = len(parts)
            for i in range(0, nparts):
                inc = int(parts[i])*pow(-1, nparts-1-i)
                sum = sum + inc
            answer = divisible(sum, d)
        elif 8 == d:
            answer = divisible(s[-3:], 8)
        elif 10 == d:
            answer = s[-1] == '0'
        elif 17 == d:
            answer = divisible(int(s[:-1])-5*int(s[-1]), 17)
        elif 19 == d:
            answer = divisible(int(s[:-1])+2*int(s[-1]), 19)
        elif 23 == d:
            answer = divisible(int(s[:-1])+7*int(s[-1]), 23)
    table[(n,d)] = answer
    return answer

def test_divisible():
    import numpy as np
    OK = True
    for i in range(0, 100000):
        for j in (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23):
            x = divisible(i, j)
            if x is True:
                try:
                    assert( np.mod(i, j) == 0)
                except:
                    OK = False
                    print(i, j, x)
            else:
                try:
                    assert( np.mod(i, j) != 0)
                except:
                    OK = False
                    print(i, j, x)
    if OK:
        print('OK')

#test_divisible()
