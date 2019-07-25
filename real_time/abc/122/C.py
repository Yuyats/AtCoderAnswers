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

N, Q = LI()
S = input()
"""
ACのインデックスをすべて記録しておき、始点、終点で区切って出す
少ない方を取ったほうがいいかな
"""
ACs = []
for sidx in range(0, len(S)-1):
    if S[sidx] == 'A':
        if S[sidx+1] == 'C':
            ACs.append(sidx)

#  print(ACs)

LR = []
for i in range(Q):
    LR.append(LI())

#  N, Q = 10**5, 10**5
#  S = 'ACTCTTCGTG'*10**4
#  LR = []
#  for i in range(Q):
#      LR.append([3,9000])

#  for l, r in LR:
#      tmp = S[l-1:r]
#      print(tmp.count('AC'))

result = []
#  print(ACs)
for l, r in LR:
    start = bisect.bisect_left(ACs, l-1)
    end = bisect.bisect_left(ACs, r-1)
    #  print('s,e', start, end)
    print(end-start)
