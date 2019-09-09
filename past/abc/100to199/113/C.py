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
P, Y = [], []
for i in range(M):
    j, k = LI()
    P.append(j)
    Y.append(k)

#  N = 10**5
#  M = 10**5
#  P, Y = [], []
#  for i in range(M):
#      P.append(10)
#      Y.append(i*100)

city_records = [[]for i in range(10**6)]
for p, y in zip(P, Y):
    #  print('p,y', p, y)
    #  print('city_records[p]', city_records[p])
    city_records[p].append(y)

#  print(city_records)

for i in range(len(city_records)):
    if city_records[i] == []:
        continue
    city_records[i].sort()

#  print(city_records)

for p, y in zip(P, Y):
    #  order = (city_records[p].index(y)) + 1
    order = bisect.bisect_left(city_records[p], y) + 1
    print(str(p).zfill(6) + str(order).zfill(6))
