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

s = input()
K = I()
#  s = ''.join(['a' if i % 2 == 0 else 'b' for i in range(5000)])
#  K = 1

combis = []
for i in range(1, K+1):
    start = 0
    while start+i <= len(s):
        combi = s[start:start+i]
        combis.append(combi)
        start += 1
#  print(combis)
combis = list(set(combis))
combis = sorted(combis)
print(combis[K-1])

#  # 単位をあげていく
#  # 1つのとき、２つのとき、３つのとき
#  combis = []
#  length = len(s)
#  while True:
#      if length == 0:
#          break
#      current_idx = 0
#      while current_idx + length <= len(s):
#          combi = s[current_idx:current_idx+length]
#          if combi not in combis:
#              combis.append(combi)
#          current_idx += 1
#      #  print('combis', combis)
#      length -= 1
#  combis = sorted(combis)
#  #  print(combis)
#  print(combis[K-1])
