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
def pf(s): return print(s, flush=True)

N = I()

l = []
for i in range(5):
    l.append(I())

min_value = min(l)
hoge = math.ceil(N / min_value)
#  print(hoge)
print(hoge+4)
#  counts = [N,0,0,0,0,0]
#  result = 0
#  while counts[-1] != N:
#      tmp = [_ for _ in counts]
#      for c in reversed(range(1, 6)):
#          if counts[c-1] > 0:
#              change = min(l[c-1], counts[c-1])
#              counts[c-1] -= change
#              counts[c] += change
#      print(counts)
#      result += 1
#  print(result)
