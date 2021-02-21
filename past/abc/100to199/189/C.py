#  import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
import sys

inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
#  def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI(): return list(map(int, input().split()))
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)


N = _I()
A = LI()


"""
範囲内の最小値がxとなる
r-lをかけたものの最大値を求める

l,rの組み合わせは10**4*10**4

範囲内の最小を求める

xを固定する
"""

ans = 0
for l in range(0, N):
    mn = inf
    for r in range(l, N):
        #  print(l, r, mn, A[r])
        mn = min(A[r], mn)
        ans = max((r - l + 1)*mn, ans)
        #  print(ans)

print(ans)
