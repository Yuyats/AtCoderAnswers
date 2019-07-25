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

S = S()
#  S = ''
#  for i in range(10**5):
#      if i % 2 == 0:
#          S += '011'
#      else:
#          S += '1'
#  S = '011'*100000

#  print(S)
result = 0
# 0と1すくない方の数になる絶対
print(min(S.count('1'), S.count('0'))*2)
#  while True:
#      print('loop;')
#      if S.find('01') < 0 and S.find('10') < 0:
#          print(result)
#          exit()
#      if S.find('01') >= 0:
#          idx = S.find('01')
#          S = S[:idx] + S[idx+2:]
#          result += 2

#      if S.find('10') >= 0:
#          idx = S.find('10')
#          S = S[:idx] + S[idx+2:]
#          result += 2


