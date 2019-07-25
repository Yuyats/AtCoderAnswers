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
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def pf(s): return print(s, flush=True)

S = input()
# 2通り試せばいい
# 最初を0にするか1にするか
current = '0'
ans1 = 0
for s in S:
    if s == current:
        if current == '0':
            current = '1'
        else:
            current = '0'
    else:
        # 塗り直し
        if current == '0':
            current = '1'
        else:
            current = '0'
        ans1 += 1

current = '1'
ans2 = 0

for s in S:
    if s == current:
        if current == '0':
            current = '1'
        else:
            current = '0'
    else:
        # 塗り直し
        if current == '0':
            current = '1'
        else:
            current = '0'
        ans2 += 1

print(min(ans1, ans2))
