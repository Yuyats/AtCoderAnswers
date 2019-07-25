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
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def pf(s): return print(s, flush=True)

v = []
for i in range(5):
    v.append(I())

# 全探索？
# 1の位が一に一番近いものを求める
str_v = [str(i) for i in v]
min_first_digit = None
for sidx, s in enumerate(str_v):
    if s[-1] == '0':
        continue
    if min_first_digit == None:
        min_first_digit = [sidx , s[-1]]
        continue
    if s[-1] < min_first_digit[1]:
        min_first_digit = [sidx, s[-1]]

if min_first_digit == None:
    print(sum(v))
else:
    result = 0
    for vidx, item in enumerate(v):
        if vidx != min_first_digit[0]:
            result += item
            if item % 10 != 0:
                result += 10 - item % 10
    result += v[min_first_digit[0]]
    print(result)
