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

N, x = LI()
A = LI()
original_sum = sum(A)
for aidx in range(N-1):
    if A[aidx] + A[aidx+1] <= x:
        continue
    else:
        diff = A[aidx] + A[aidx+1] - x
        sub = min(diff, A[aidx+1])
        A[aidx+1] -= sub
        diff -= sub
        if diff > 0:
            A[aidx] -= min(A[aidx], diff)

#  print(A)
ans = original_sum - sum(A)
print(ans)
