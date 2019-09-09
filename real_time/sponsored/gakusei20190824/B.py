import math, string, itertools, fractions, heapq, collections, re, \
array, bisect, sys, random, time, copy, functools, os, queue, pdb
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
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)

N, K = LI()
A = LI()

from fractions import Fraction
"""
2 1なら
2 1 2 1
点灯数は、左の数のほうが多いもの
2 1
2 1
2 1
の3種類
2回つなげてみたら決まる
2 1 2 1なら
K = 2で3
K=3 で 2 1 2 1 2 1で6
K=4 で2 1 2 1 2 1 2 1で10通り 4+3+2+1=
K=6なら 2 1 2 1 2 1 2 1 2 1 2 1で6+5+4+3+2+1 =

偶奇でわける
modで割る

1 2なら
1 2 1 2で1しかない1
1 2 1 2 1 2なら3で2 + 1
1 2 1 2 1 2 1 2 なら6で3+2+1
"""
if len(set(A)) == 1:
    print(0)
    exit()

"""
各数字ごとに数える
"""
K %= mod
in_count = 0
for i in range(N):
    for j in range(i, N):
        if A[i] > A[j]:
            #  print('i, j', i,j, A[i], A[j])
            in_count += 1
#  print(in_count)
in_count %= mod
in_ans = in_count * K
in_ans %= mod

out_count = 0
for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            out_count += 1
#  print(out_count)

out_count %= mod
#  out_ans = (out_count * K * (K-1))//2
#  out_ans = out_count * (((K * (K-1))%mod)/2) % mod
out_ans = int(Fraction(out_count) * Fraction(K) * Fraction(K-1) / Fraction(2))
out_ans %= mod
#  print(in_ans, out_ans)
print(int((in_ans + out_ans)%mod))

#  count_list = [[0,0] for _ in range(N)]
#  for i in range(N):
#      a_count = 0
#      for j in range(N):
#          if A[i] > A[j]:
#              # でかいときはメモ？
#              count_list[i][0] += 1
#      for j in range(0, i):
#          if A[i] > A[j]:
#              count_list[i][1] += 1

#  print(count_list)
#  ans = 0
#  for c in count_list:
#      print('c', c)
#      ans += ((c[0]*K*(K+1)-K*c[1])/2)%mod
#      print(ans)
#  print(int(ans%mod))

#  #  a_count = 0
#  #  for i in range(N):
#  #      for j in range(i, N):
#  #          if A[i] > A[j]:
#  #              a_count += 1
#  #  print(a_count)
#  #  if a_count == 0:
#  #      new_A = A + A
#  #      new_a_count = 0
#  #      for i in range(N*2):
#  #          for j in range(i, N*2):
#  #              if new_A[i] > new_A[j]:
#  #                  a_count += 1
#  #      ans = (1/2)*(K-1)*K*a_count
#  #  else:
#  #      ans = (1/2)*K*(K+1)*a_count
#  #  print(int(ans)%mod)
    
#  #  s = A + A
#  #  c = 0
#  #  for i in range(0, N*2-1):
#  #      if s[i] > s[i+1]:
#  #          c += 1
#  #  print(c)
#  #  #  if K % 2 == 0:
#  #  #      # 偶数の場合は
#  #  #      m = int(K / 2)
#  #  #      ans = c*m
#  #  #      ans = (1/2)*ans*(ans + 1)
#  #  #      #  ans = sum([i for i in range(1,ans+1)])
#  #  #      print(ans%mod)
#  #  #  else:
#  #  #      # 奇数
#  #  #      #  K -= 1
#  #  #      m = int(K/2)
#  #  #      ans = c*m
#  #  #      ans = (1/2)*ans*(ans + 1)
#  #  #      #  ans = sum([i for i in range(1, ans+1)])
#  #  #      #  ans += c
#  #  #      print(ans%mod)
