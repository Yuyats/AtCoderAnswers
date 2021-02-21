import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools

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

"""
0からkまで探索
組み合わせ
あまりを求める
"""
str_N = str(N)
N_items = [int(i)%3 for i in str_N]
total = sum(N_items) % 3
if total == 0:
    print(0)
elif total == 1:
    if 1 in N_items:
        if len(N_items) == 1:
            print(-1)
        else:
            print(1)
    else:
        if len(N_items) == 2:
            print(-1)
        else:
            print(2)
else:
    if 2 in N_items:
        if len(N_items) == 1:
            print(-1)
        else:
            print(1)
    else:
        if len(N_items) == 2:
            print(-1)
        else:
            print(2)
