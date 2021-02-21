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

N, K = LI()
T = [LI() for i in range(N)]

"""
Nが小さいので全通り
"""
ans = 0
def dfs(visited, unvisited, t, current_city):
    global ans
    #  print(visited, unvisited, t)
    if len(visited) == N:
        t += T[current_city][0]
        if t == K:
            #  print('========')
            ans += 1
        return

    for u in unvisited:
        tmp_unvisited = [u for u in unvisited]
        new_visited = visited + [u]
        tmp_unvisited.remove(u)
        dfs(new_visited, tmp_unvisited, t + T[current_city][u], u)



tmp = [j for j in range(1, N)]
dfs([0], tmp, 0, 0)
print(ans)
