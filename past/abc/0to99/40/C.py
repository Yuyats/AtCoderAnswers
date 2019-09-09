import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools,pdb
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

N = _I()
A = LI()
#  A += [A[-1], A[-1]]

"""
なるべく差がすくないように移動したい
1 2 2 2
1 1 1 2 2 2などが考えられる

Nが10**5なので、全通り試すのは無理がある
まずは各場所から1,2個先とのコストは出しといたほうが良さそう
普通にdfsでやればいいか。
そしたら大体
全部2ステップの場合
1個だけ1ステップの場合
...
全部1ステップの場合
それぞれ10**5通りある
さらにそれらの並び替えとすると
10**5Ck通りずつある


最大のところを飛ばすようにやればいいのでは？
1個飛ばしと2個飛ばしの距離のリストをもつ
最大のところは使わないようにする
そうすると使わないところの移動手段が決まる
dpだった
なるほど
"""
dp = [None]*(N+1)
dp[0] = 0
dp[1] = 0
dp[2] = abs(A[0] - A[1])
# 1本目の柱からi本目までのコスト
for i in range(3, N+1):
    val1 = dp[i-1] + abs(A[i-1] - A[i-1-1])
    val2 = dp[i-2] + abs(A[i-1] - A[i-2-1])
    dp[i] = min(val1, val2)
#  print(dp)
print(dp[N])


#  A1 = []
#  A2 = []
#  steps = [None] * (N-1)
#  for aidx in range(N-1):
#      val1 = abs(A[aidx] - A[aidx+1])
#      A1.append(val1)
#      if aidx != N-2:
#          val2 = abs(A[aidx] - A[aidx+2])
#          A2.append(val2)
#  print(A1, A2)
#  while any(i is None for i in steps):
#      print(steps, A1, A2)
#      A1_min = min(A1)
#      A2_min = min(A2)
#      if A1_min < A2_min:
#          # 1歩ずつ進むほうがコストが高い場合、その1歩はとばす
#          idx = A1.index(A1_min)
#          steps[idx] = A1_min
#          A1[idx] = inf
#          if idx <= N-3:
#              A2[idx] = inf
#          A2[idx-1] = inf
#      else:
#          # 2歩進む
#          idx = A2.index(A2_min)
#          steps[idx] = A2_min
#          steps[idx+1] = 0
#          A2[idx] = inf
#          A2[idx-1] = inf
#          A1[idx] = inf
#          A1[idx+1] = inf
#  print(sum(steps))






#  ans = 0
#  skip = False
#  for aidx in range(N):
#      if skip:
#          skip = False
#          continue
#      else:
#          val1 = abs(A[aidx] - A[aidx+1])
#          val2 = abs(A[aidx] - A[aidx+2])
#          if val1 > val2:
#              # 2保進む
#              skip = True
#              ans += val2
#          else:
#              ans += val2
    
#  A = A[:-2]
#  A = list(reversed(A))
#  A += [A[-1], A[-1]]
#  skip = False
#  ans2 = 0
#  for aidx in range(N):
#      if skip:
#          skip = False
#          continue
#      else:
#          val1 = abs(A[aidx] - A[aidx+1])
#          val2 = abs(A[aidx] - A[aidx+2])
#          if val1 > val2:
#              # 2保進む
#              skip = True
#              ans2 += val2
#          else:
#              ans2 += val2
#  ans = min(ans, ans2)
#  print(ans)
#  #  ans = inf
#  #  def dfs(position, cost):
#  #      global ans
#  #      if position >= N-1:
#  #          # 最後までたどり着いた
#  #          ans = min(ans, cost)
#  #          return
#  #      val1 = abs(A[position] - A[position+1])
#  #      dfs(position+1, cost + val1)
#  #      val2 = abs(A[position] - A[position+2])
#  #      dfs(position+2, cost + val2)
#  #  dfs(0, 0)
#  #  print(ans)
