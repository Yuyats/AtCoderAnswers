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
1,2,3...の並びになっている必要がある
並び順が昇順ではない数字をカウントしていく
もしくは、1から順番に探していく
"""

current_idx = 0
ans = 0
for i in range(1, N + 1):
    for j in range(current_idx, N):
        # 前回見つかった場所の右隣から再開
        if A[j] == i:
            current_idx = j + 1
            ans += 1
            break
    else:
        # iに一致するアイテムはないので、以上
        break
if ans == 0:
    print(-1)
else:
    print(N - ans)
