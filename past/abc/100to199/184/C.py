import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
from decimal import *

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

r1, c1 = LI()
r2, c2 = LI()
diffs = [-3, -2, -1, 0, 1, 2, 3]
r = r2 - r1
c = c2 - c1

if r1 == r2 and c1 == c2:
    # 0手の場合
    ans = 0
elif r == c or r == -c:
    ans = 1
elif abs(r1 - r2) + abs(c1 - c2) <= 3:
    # 1手の場合
    ans = 1
# 2手の場合
#  elif ((r1 - r2) ^ (c1 - c2) ^ 1) & 1:
elif abs(r1 - r2) % 2 ==  abs(c1 - c2) % 2:
    # グリッドに入っている場合
    ans = 2
elif abs(r1 - r2) + abs(c1 - c2) <= 6:
    # 距離が6以内の場合
    ans = 2

#  elif abs(r + c) <= 3 or abs(r - c) <= 3:
elif any(c2 == r2 + c1 - r1 + i for i in diffs):
    # 点Aから傾き1、切片-3~3の間に点Bがある場合は2手
    ans = 2
elif any(c2 == -r2 + c1 + r1 + i for i in diffs):
    ans = 2
else:
    ans = 3

print(ans)
