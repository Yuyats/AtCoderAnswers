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

S = I()
K = I()

if len(list(set(str(S)))) == 1:
    print(str(S)[0])
    exit()

first_non_one_number = None
for idx, i in enumerate(str(S)):
    if i != '1':
        first_non_one_number = idx
        break

if K-1 < first_non_one_number:
    print(1)
    exit()
else:
    print(str(S)[first_non_one_number])
#  time = 5*10**15

#  points = []
#  count = 0
#  for s in str(S):
#      print(s)
#      count += int(s)**time
#      print('count', count)
#      points.append(count)
#  print(points)
#  for idx, p in enumerate(points):
#      if K < p:
#          print(str(S)[idx])
#          break
