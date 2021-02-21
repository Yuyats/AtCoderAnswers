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


X, K, D = LI()


dist = K * D
#  print(dist)
X = abs(X)

if X == 0:
    # Kのパリティで切り分け
    if K % 2 == 0:
        print(0)
    else:
        print(D)
elif X > dist:
    print(X - dist)
elif X == dist:
    print(0)
elif X < dist:
    # 元いた場所から原点を超えて移動できる場合
    y = X // D
    L = [X - D * y, abs(X - D * y - D)]
    if (K - y) % 2 == 0:
        print(L[0])
    else:
        print(L[1])
