#  import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
#  sys.setrecursionlimit(10**7)
#  inf = 10 ** 20
#  eps = 1.0 / 10**10
#  mod = 10**9+7
#  dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#  ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
#  def LI(): return [int(x) for x in sys.stdin.readline().split()]
#  def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
#  def LF(): return [float(x) for x in sys.stdin.readline().split()]
#  def LS(): return sys.stdin.readline().split()
#  def I(): return int(sys.stdin.readline())
#  def F(): return float(sys.stdin.readline())
#  def S(): return input()
#  def pf(s): return print(s, flush=True)

#  N, K = LI()
#  A = LI()

#  if N == K:
#      print(1)
#      exit()
#  N -= K
#  result = N / (K-1) + 1
#  if result % 1 != 0:
#      result //= 1
#      result += 1

#  print(int(result))



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

N, K = LI()
A = LI()

if N == K:
    print(1)
    exit()
result = 0
N -= K
result += 1
result += N / (K-1)
if N % (K-1) != 0:
    result = int(result) + 1

print(int(result))
