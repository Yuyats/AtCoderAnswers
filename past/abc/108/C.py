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

"""
単体のみで目的の数になる数字を数える
その数のみの組み合わせ + その数と他の数の組み合わせでできるものを求める
偶数の場合と奇数の場合で変わってくる
奇数の場合、同じ数同士での組み合わせは作れない
5,3の場合、3/3/3しかない
5,5の場合、5/5/5
10, 5の場合、5/5/5, 5/5/10, 5/10/10,など
奇数の場合、Kは作れない。
Kの倍数のみ作れる
3
"""

#  N, K = LI()
#  K_list = []

#  if K%2 == 0:
#      # 偶数
#      # すべてi%K == 0かすべてi%K == K/2であるかのどちらかである
#      result = (N/K)**3
#      result += (N/(K//2))**3
#      print(result)
#  else:
#      # 奇数
#      print((N//K)**3)

def iin(): return int(input())
def nl(): return list(map(int, input().split()))
def ary(r, c, v): return [[v for _ in range(c)] for _ in range(r)]

n, k = nl()

d = dict()
for i in range(1, n + 1):
    t = i % k
    d[t] = d.get(t, 0) + 1
#  print(d)
ans = 0
if k % 2 == 0:
    #  import pdb,gnureadline
    #  pdb.set_trace()
    ans += d.get(k // 2, 0) ** 3
ans += d.get(0, 0) ** 3
print(ans)
