import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools, os, queue
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
def perr(s): return print(s, file=sys.stderr)


N, M = LI()
AB = []
for i in range(N):
    AB.append(LI())
# 日付ごとに報酬をまとめる
AB_dict = {}
for ab in AB:
    if ab[0] not in AB_dict.keys():
        AB_dict[ab[0]] = [ab[1]]
    else:
        AB_dict[ab[0]].append(ab[1])

ans = 0
pq = queue.PriorityQueue()
keys = AB_dict.keys()
for i in range(1, M+1):
    # 残りi日
    if i in keys:
        for ab in AB_dict[i]:
            # 最大値から取り出したいので以下のように入れていく
            pq.put((-ab, ab))
    if pq.empty():
        continue
    ans += pq.get()[1]
print(ans)
