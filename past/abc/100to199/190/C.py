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

N, M = LI()
AB = [LI() for i in range(M)]

K = _I()
CD = [LI() for i in range(K)]


"""
全通り試す場合
16人の投票。
2の16乗通65000通り程度。
全通り調べ、どれが最大かを確認する
100通り
6.5*10**5なので間に合う
"""


def dfs(idx, items):
    #  print(items)
    if idx == K:
        global ans
        count = 0
        for a, b in AB:
            if a in items and b in items:
                count += 1
        ans = max(ans, count)
        return

    next_idx = idx + 1
    dfs(next_idx, items + [CD[idx][0]])
    dfs(next_idx, items + [CD[idx][1]])



ans = 0
dfs(0, [])
print(ans)
