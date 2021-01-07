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

N, M = LI()
A = LI()
if len(A) == N:
    print(0)
    exit()

if M == 0:
    print(1)
    exit()

A.sort()
"""
間が一番狭いところを探せば良い？？？
それでは無理。
6 4 4
のとき
k=4で
4 4 6 6
とすると3回
"""

#  print(A)
diffs = []
for aidx, a in enumerate(A):
    if aidx == 0:
        # 0からの距離
        diff1 = a - 1
        diff2 = abs(a - A[aidx+1]) - 1
        diffs.append(diff1)
        diffs.append(diff2)
        continue
    elif aidx == len(A) - 1:
        # 最後の要素の場合、Nからの距離
        diff = N - a
        #  print(diff)
        if diff == 0:
            continue
    else:
        diff = abs(a - A[aidx+1]) - 1
    #  print('diff', diff)
    diffs.append(diff)

diffs.sort()

diffs = [i for i in diffs if i != 0]
min_diff = diffs[0]
#  print('min_diff', min_diff)
#  print('diffs', diffs)

ans = 0
for i in diffs:
    ans += math.ceil(Decimal(i)/Decimal(min_diff))
print(ans)
