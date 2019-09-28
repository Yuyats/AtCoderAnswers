import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
sys.setrecursionlimit(10**7)
from queue import PriorityQueue
from fractions import gcd
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

N,K = LI()
A = LI()
'''
ずらしていく
5 3なら
1 2 3 4 5
1 2 3 
2 3 4
3 4 5

と5-3+1個ある
重複する部分が
1 2 3 ... K ... 3 2 1
となる
2*1/2*K*(K+1) - K

5 3
1 2 4 8 16
1 2 4
  2 4 8
    4 8 16
なら
1 + 4 + 12 + 16 + 16 = 49

5 4なら
1 2 4 8
  2 4 8 16
32+12+1=45

5 2
1 2
  2 4
    4 8
      8 16
1 2 2 2 1
1+4+8+16+16
=45

'''
#  print(K*(K+1) - K)
ans = 0
#  for i in range(1, K+1):
#      ans += A[i-1] * i
#  A = A[::-1]
#  print(A)
#  for i in range(1, K):
#      ans += A[i-1] * i

if N - K + 1 <= K:
    # 全体に行き渡らない場合。範囲が長い場合、累積wa
    cumsums = [0]
    for a in A:
        cumsums.append(cumsums[-1] + a)
    for i in range(K, K + N-K+1):
        ans += cumsums[i] - cumsums[i-K]
    #  print(cumsums)
else:
    # 何個連続してる箇所があるか計算。左からK-1個、右からK-1個は同じになる。残りがK個ずつ
    for i in range(0, K-1):
        ans += A[i] * (i+1)
    #  print(ans)
    A = A[::-1]
    #  print(A)
    for i in range(0, K-1):
        ans += A[i] * (i+1)
    #  print(ans)
    # 真ん中を足す
    #  print(A[K-1:-K+1])
    for a in A[K-1:-K+1]:
        ans += a*K

#  cumsums = [0]
#  for a in A:
#      cumsums.append(cumsums[-1] + a)
#  for i in range(K, K + N-K+1):
#      ans += cumsums[i] - cumsums[i-K]

print(ans)
