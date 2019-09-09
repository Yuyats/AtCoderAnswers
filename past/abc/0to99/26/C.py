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

N = _I()
B = [_I() for _ in range(N-1)]

"""
主従関係を作る
1を持つものから辿っていく
高橋くんの給料しか求めなくて良いので、
下から数えていく形
N番目のものが一番低い
1 2 3は上司の社員番号
"""
d = {}
for i in range(1, N+1):
    d[i] = []

for bidx, b in enumerate(B):
    d[b].append(bidx+2)


#  print(d)
ans = [0] * (N+2)

def dfs(num):
    #  print(num)
    if len(d[num]) == 0:
        # 部下いないので給料1
        ans[num] = 1
        return

    # 給料を最終的に返すことで再帰的に一番上の給料を計算する
    max_sal = 0
    min_sal = inf
    for i in d[num]:
        #  print('i ', i)
        # 部下の給料を計算
        dfs(i)
        max_sal = max(max_sal, ans[i])
        min_sal = min(min_sal, ans[i])
    ans[num] += max_sal + min_sal + 1
dfs(1)
print(ans[1])
