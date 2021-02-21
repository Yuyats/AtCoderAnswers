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

XY = [LI() for i in range(N)]

P = list(itertools.permutations([i for i in range(N)], N))
#  print(P)
t = 0
for p in P:
    d = 0
    for i in range(N):
        if i == 0:
            continue
        else:
            # 前の町との距離
            XY1 = XY[p[i]]
            XY2 = XY[p[i-1]]
            s = math.sqrt((XY1[0]-XY2[0])**2+(XY1[1]-XY2[1])**2)
            d += s
    else:
        t += d

print(t/len(P))
