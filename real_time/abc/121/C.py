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
def S(): return input()
def pf(s): return print(s, flush=True)


N, M = LI()

AB = []
for i in range(N):
    a,b = LI()
    AB.append([a, b])



# ただ安い店から買い叩いていくだけの話
AB = sorted(AB, key=lambda x:x[0])
#  print(AB)


count = 0
idx = 0
cost = 0
while count < M:
    #  print('idx', idx)
    if AB[idx][1] > M - count:
        # この店で終わりの場合
        cost += (M-count)*AB[idx][0]
        count = M
        break
    else:
        # 全部買う
        cost += AB[idx][0] * AB[idx][1]
        count += AB[idx][1]
    idx += 1

print(cost)
