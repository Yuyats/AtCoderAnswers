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
def _pf(s): return print(s, flush=True)

N = _I()
A = []
for i in range(N):
    A.append(_I())

max_v = max(A)
max_v_count = A.count(max_v)
if max_v_count >= 2:
    # どれをとっても最大は最大
    for a in A:
        print(max_v)
else:
    for a in A:
        if a == max_v:
            second_max_v = [_ for _ in A]
            second_max_v.remove(max_v)
            second_max_v = max(second_max_v)
            print(second_max_v)
        else:
            print(max_v)
