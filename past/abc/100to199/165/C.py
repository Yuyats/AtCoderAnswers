import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools

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

"""
1-10なので
組み合わせは2**10=1024通り
それぞれの点数を計算すればよい
毎回50通りの確認をはさむ
"""

N, M, Q = LI()
X = [LI() for i in range(Q)]

#  ans = 0
#  def dfs(count, arr):
#      # 終了条件
#      if count == N:
#          # 点数計算
#      else:
#          # 選ぶ
#          dfs(count+1, arr)
#          dfs(count+1, arr+[])


#  dfs(0, [])
#  print(ans)

ans = 0

combis = list(itertools.combinations_with_replacement([i for i in range(1, M+1)], N))
#  combis = list(itertools.combinations([i for i in range(1, M+1)], N))
#  print(combis)

for combi in combis:
    #  print('combi', combi)
    tmp_ans = 0
    for x in X:
        #  print('x', x)
        if combi[x[1]-1] - combi[x[0]-1] == x[2]:
            tmp_ans += x[3]
    else:
        #  print('tmp', tmp_ans)
        ans = max(ans, tmp_ans)
print(ans)
