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

N, M, X = LI()
CA = [LI() for i in range(N)]
#  print(CA)

"""
すべての参考書の組み合わせを求めると、
参考書は最大12冊なので
2**12=4096通りしかないので全通り確かめる
"""


ans = inf
def dfs(cost, points, idx):
    if idx == N:
        global ans
        # すべての参考書の状態を決め終わったので判定
        if all(i >= X for i in points):
            ans = min(ans, cost)
        return
    else:
        # idxの参考書の状態を渡す
        # 使わない場合
        dfs(cost, points, idx+1)
        # 使う場合
        dfs(cost + CA[idx][0], [points[i]+CA[idx][i+1] for i in range(M)],idx+1)



dfs(0, [0]*M, 0)
if ans == inf:
    ans = -1
print(ans)
