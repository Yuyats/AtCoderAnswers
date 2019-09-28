import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
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
N, K = LI()
P = LI()

des_list = []
for pidx in range(N-1):
    # 逆順を求める
    if P[pidx] > P[pidx+1]:
        # 後のほうが小さい場合
        des_list.append(1)
    else:
        des_list.append(0)
print(des_list)
'''
0101でK=3なら
2こずつで進んでいく
01
10
01
なので、
気をつけるべきは、同じ1をひっくりかえしてもあかん
01
010010なら
01
10
00
10
'''
for idx in range(N):

