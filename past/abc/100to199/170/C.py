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

X, N = LI()
P = LI()
P.sort()
#  print(P)

min_diff = 1010
ans = 100
"""
1
0 1 2 3
-1 なら2
4 なら3
"""
for i in range(-1, 102):
    if i in P:
        pass
    else:
        diff = abs(X-i)
        #  print(diff)
        if diff == min_diff:
            if ans > i:
                ans = i
        elif  diff < min_diff:
            min_diff = diff
            ans = i
print(ans)
