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
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)

N, K = LI()
"""
青いボールがK個、赤いボールがN-K個
まずiを回す
1の時、左端がどこにあるかで
5 3なら
BBBRR
RBBBR
RRBBB
の3通り
2のとき、
1/2と2/1の分け方がある
仮に1をA、2をBとすると
赤2とA,Bを並び替える
つまり、4!/2!1!1! = 6通り
1 1 1のときは

"""





# 1かいてことは、青を全部つなげた上で、1+N-K個の並べ替え
# 2かいてことは、青の分け方で1通り、1/2。それを3この赤と並べ替えるから、5!/1*1*3! = 5*4*3*2*1/3*2*1 = 10
# これから、隣り合う場合を引かなければならないので、4!/1*3! = 4通りを引く
# 3回ってことは、全て違う場合。1通り
#  res = []
#  for i in range(1,K+1):
#      if N-K+1 < i:
#          res.append(0)
#          continue
#      # i回の場合
#      # 分ける箇所は、N-K+1Ci
#      # 分け方は、K+1Ciとなる。
#      n = N-K+1
#      k = i
#      #  print(i)
#      ans1 = math.factorial(n)/(math.factorial(k) * math.factorial(n-k))

#      n = K - i + 1
#      k = i - 1
#      n = K - 1
#      k = i - 1
#      ans2 = math.factorial(n)/(math.factorial(k) * math.factorial(n-k))

#      res.append(ans1*ans2)
#  for i in res:
#      print(int(i%mod))

