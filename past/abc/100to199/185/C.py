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

L = _I()

upper = [i for i in reversed(range(1, L))][:11]
lower = [i for i in range(1, 12)]

upper_value = 1
for i in upper:
    if not i in lower:
        upper_value *= i
lower_value = 1
for i in lower:
    if not i in upper:
        lower_value *= i
print(upper, lower)
print(upper_value, lower_value)

ans = upper_value//lower_value
print(upper_value/lower_value)
print(int(Decimal(upper_value)/Decimal(lower_value)))
#  ans = int(upper_value//lower_value)
print(ans)
