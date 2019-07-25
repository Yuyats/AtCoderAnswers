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


"""
解説を読んで

最終的に行き着く数をXとする
XはA,B,Cの最大値または最大値＋１のどちらかである。
そうすると、3X - (A+B+C)を2で割った時に余り0となるようなXを求めれば良い
それはA,B,Cの最大値またはそれにプラス１した値である。

"""
A, B, C = LI()
X = max(A,B,C)
result1 = 3*X - (A+B+C)
result2 = 3*(X+1) - (A+B+C)
if result1%2 == 0:
    print(int(result1/2))
else:
    print(int(result2/2))

#  nums = sorted([A,B,C])
#  set_nums = list(set([A,B,C]))
#  result = 0
#  if len(set_nums) == 1:
#      print(0)
#  elif len(set_nums) == 2:
#      # 2種類は一緒
#      #前２つが一緒かつはぐれが大きい
#      if nums[0] == nums[1]:
#          result += nums[2]-nums[1]
#          print(result)
#          exit()
#      elif nums[1] == nums[2]:
#          # 後ろ２つが等しく、はぐれが最小
#          result += (nums[1] - nums[0])//2
#          if (nums[1]-nums[0]) % 2 != 0:
#              result += 2
#          print(result)
#          exit()
#  else:
#      # 全数字が異なる
#      result += nums[2]-nums[1]
#      nums[0] += nums[2]-nums[1]
#      result += (nums[2] - nums[0]) // 2
#      if (nums[2] - nums[0]) % 2 != 0:
#          result += 2

#      print(result)

