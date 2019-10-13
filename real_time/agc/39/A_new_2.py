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
"""
なかのものと端のもの
両端が一緒かどうか
一緒なら、K-1個変える
中を変える/2切り下げ
まず、端が一緒か
"""
S = input()
K = _I()
ans = 0

if len(set(S)) == 1:
    print(int(math.floor(len(S)*K/2)))
    exit()

S2 = S*2
S3 = S*3

torn_list_1 = []
previous = 'hoge'
for s in S2:
    if s == previous:
        torn_list_1[-1] += 1
    else:
        torn_list_1.append(1)
        previous = s
torn_list_2 = []
previous = 'hoge'
for s in S3:
    if s == previous:
        torn_list_2[-1] += 1
    else:
        torn_list_2.append(1)
        previous = s

ans2 = 0
ans3 = 0
for t in torn_list_1:
    if t>=2:
        ans2+=int(math.floor(t/2))

for t in torn_list_2:
    if t>=2:
        ans3+=int(math.floor(t/2))

diff = ans3-ans2

ans = ans2 + (K-2)*diff
print(ans)
