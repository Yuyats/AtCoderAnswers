import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
import numpy
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


K = _I()

"""
7,77,777,...
=7,7*10+7,7*100+7*10+7,...
K<=10**6
むしろKを倍にしていったほうがはやい？

101*77=7777
K*x=sum(7,70,700,7000)
"""

#  a = 7 % K
#  if a == 0:
#      print(1)
#      exit()

#  for i in range(1, K):
#      a = (10 * a + 7) % K
#      if a == 0:
#          print(i+1)
#          exit()
#  else:
#      print(-1)


a = 7
for i in range(1, K):
    #  a = 10 * a + 7
    a *= 2
    #  print(i)
    #  if a % K == 0:
    #      print(i+1)
    #      exit()
else:
    print(-1)


