import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools, os, pdb
sys.setrecursionlimit(10**7)
from queue import PriorityQueue
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
def perr(s): return print(s, file=sys.stderr)

N = _I()
S = [_I() for _ in range(N)]

for s in S:
    s = [int(i) for i in str(s)]
    counts = collections.Counter(s).most_common()
    if len(set(s)) == 1:
        print("Four Card")
    elif counts[0][1] == 3:
        print("Three Card")
    elif counts[0][1] == 2:
        if counts[1][1] == 2:
            print('Two Pair')
        else:
            print("One Pair")
    else:
        print("No Pair")

