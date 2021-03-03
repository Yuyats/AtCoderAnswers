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

N,M,K = LI()
A = LI()
B = LI()
"""
累積和
iを固定で0からNまでループ
jを固定でMから0までループ
jは前回の値から開始

iだけでKを超えてしまう場合はiなしでチェック
"""

cum_a = [0] + list(numpy.cumsum(A))
cum_b = [0] + list(numpy.cumsum(B))
#  print(cum_a, cum_b)

ans = 0
for i in range(N+1):
    #  print('i', i)
    now = cum_a[i]
    if now > K:
        # AだけでKを超えている場合は終了
        ans = max(i - 1, ans, 0)
        #  print('ans first', ans)
        #  break
    #  else:
    # Bの本とあわせる場合、上から見ていく
    for j in range(M, -1, -1):
        #  print(' j', j, 'm', M)
        if now + cum_b[j] <= K:
            # あわせて下回るまで計算
            ans = max(i + j, ans)
            #  print('ans middle', ans)
            M = j
            #  print('middle')
            break
    else:
        # Mをぎりぎりまで減らしてもだめな場合
        ans = max(i-1, ans)
        #  print('ans last', ans)
        #  print('last')
        break
print(ans)


#  N, M, K = map(int, input().split())
#  A = list(map(int, input().split()))
#  B = list(map(int, input().split()))

#  a, b = [0], [0]
#  for i in range(N):
#      a.append(a[i] + A[i])
#  for i in range(M):
#      b.append(b[i] + B[i])
#  print(a, b)
#  ans, j = 0, M
#  for i in range(N + 1):
#      print(i)
#      if a[i] > K:
#          break
#      while b[j] > K - a[i]:
#          j -= 1
#      ans = max(ans, i + j)
#  print(ans)
