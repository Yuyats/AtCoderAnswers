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
N = _I()
A = LI()

"""
切れ目を求める
1 2 3 2 1
なら
OOOXO
1つなぎは1
2つなぎは3
3つなぎは6
4は4＋3+2+1で10
3つないでるところからは
"""
previous = -inf
clist = [0]
for a in A:
    if a > previous:
        # 大きいのでOK
        clist[-1] += 1
    else:
        #小さいので次へ
        clist.append(1)
    previous = a
#  print(clist)

ans = 0
for c in clist:
    ans += sum(range(1, c+1))
print(ans)
