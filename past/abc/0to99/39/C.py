import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
sys.setrecursionlimit(10**7)
from queue import PriorityQueue
from fractions import gcd
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)
S = input()

"""
WBWBW WBWBWBW
"""

idx = S.index('WBWBWBW')
#  print(idx)
if idx % 12 == 0:
    print('Fa')
elif idx % 12 == 1:
    print('Mi')
elif idx % 12 == 2:
    print('Re')
elif idx % 12 == 3:
    print('Re')
elif idx % 12 == 4:
    print('Do')
elif idx % 12 == 5:
    print('Do')
elif idx % 12 == 6:
    print('Si')
elif idx % 12 == 7:
    print('La')
elif idx % 12 == 8:
    print('La')
elif idx % 12 == 9:
    print('So')
elif idx % 12 == 10:
    print('So')
elif idx % 12 == 11:
    print('Fa')
