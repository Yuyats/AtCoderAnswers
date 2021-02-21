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

H, W, K = LI()
C = []
X = []
for i in range(0, H):
    C.append(input())
for c in C:
    l = []
    for i in c:
        if i == '#':
            l.append(1)
        else:
            l.append(0)
    else:
        X.append(l)
"""
全通りみるだけ
"""

ans = 0

def dfs(idx, arr):
    if idx == H + W:
        # 終了
        row_idx_list = arr[:H]
        column_idx_list = arr[H:]
        #  print('row/col', row_idx_list, column_idx_list)

        judge = [[j for j in i] for i in X]
        #  print('judge', judge)
        for r in range(H):
            if row_idx_list[r] == 1:
                judge[r] = [0]*W
                #  print('行消し', judge)
        for c in range(W):
            if column_idx_list[c] == 1:
                for j in range(H):
                    judge[j][c] = 0
        if sum([sum(y) for y in judge]) == K:
            #  print('!!!!!', judge)
            global ans
            ans += 1
        return

    arr1 = [i for i in arr]
    arr1[idx] = 1
    dfs(idx + 1, arr1)
    dfs(idx + 1, arr)


dfs(0, [0]*(H+W))
print(ans)
