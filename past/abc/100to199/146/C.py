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

A, B, X = LI()

# にぶたんする
low = 0
high = 10**9


def get_cost(n):
    return (A * n) + (B * len(str(n)))


while True:
    #  import pdb
    #  pdb.set_trace()
    #  print('low/high', low, high)
    n = low + (high - low) // 2
    cost = get_cost(n)
    #  print(cost)
    if high - low == 1:
        if X >= get_cost(high):
            print(high)
        else:
            print(low)
        exit()

    if X >= cost:
        # 買える
        low = n
    else:
        high = n
    if high == low:
        break

print(n)
