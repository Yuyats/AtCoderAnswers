import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools, pdb
sys.setrecursionlimit(10**7)
from queue import PriorityQueue
from fractions import gcd
inf, eps, mod = 10 ** 20, 1.0 / 10**10, 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)
def _cumsum(l): return list(itertools.accumulate(l))

M, N, K = LI()
A = [_I()-1 for i in range(K)]

vote_list = [0 for i in range(M)]
vote_list += [N]

for a in A:
    #  print(vote_list)
    count = 0
    for vidx, v in enumerate(vote_list):
        if vidx == a:
            pass
        else:
            if vote_list[vidx] >= 1:
                vote_list[vidx] -= 1
                count += 1
    vote_list[a] += count
#  print(vote_list)
max_v = max(vote_list[:-1])
for idx, i in enumerate(vote_list[:-1]):
    if i == max_v:
        print(idx+1)
