import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools


sys.setrecursionlimit(10**7)
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

#  N = I()

"""
先頭は1
0: 0
1: 1
10: 0 + -2 = -2
11: 1 + -2 = -1
100: 0 + 0 + 4 = 4 
101: 1 + 0 + 4 = 5
110: 0 + -2 + 4 = 2
111: 1 + -2 + 4 = 3
1000: 0 + 0 + 0 + -8 = -8
1001: 1 + 0 + 0 + -8 = -7
1010: 0 + -2 + 0 + -8 = -10
1011: 1 + -2 + 0 + -8 = -9
1100: 0 + 0 + 4 + -8 = 4
1110: 0 + -2 + 4 + -8 = -6
111
"""
#むずい
import sys
 
stdin = sys.stdin
 
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces
 
n = ni()
 
if n == 0:
    print(0)
else:
    s = ""
    while n != 0:
        #  print('n', n)
        if n % 2 != 0:
            n -= 1
            s = "1" + s
        else:
            s = "0" + s
        n //= -2
    print(s)
