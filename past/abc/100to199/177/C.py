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
A = LI()

"""
10**5
累積和
a b c d
ab ac ad
   bc bd
      cd
a * b | (a+b) * c | (a + b + c) * d
"""

C = [A[0]]
for i in range(1, N):
    C.append(C[i-1] + A[i])
#  print(C)

ans = 0
for i in range(N-1):
    ans += C[i] * A[i+1]
ans = ans % mod
print(ans)
