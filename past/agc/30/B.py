import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
from pprint import pprint


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


L, N = LI()
#  L = 10**5
#  N = 2000
X = [I() for i in range(N)]
#  X = [random.randint(1, N) for i in range(N)]

#  options = [min(L-i, i) for i in X]
#  print(options)
results = []
#  R_dp = [[0 for j in range(N)] for i in range(N)]
#  L_dp = [[0 for j in range(N)] for i in range(N)]
distances = {}
for i in X:
    for j in X:
        if i != j:
            if i >= L / 2:
                # 0地点を超える
                d = (L - i) + j
            distances[str(ij)] = d
# 距離と残りの場所を格納
histories = {'R': [X[0], X[1:], X[0]], 'L': [L - X[-1], X[:-1], X[-1]]}
def dfs(history):
    #  print(history)

    if history in histories.keys():
        # 履歴から引っ張る
        pass
    else:
        # ない場合は一個前に戻って計算
        previous = histories[history[:-1]]
        if history[-1] == 'R':
            selected = previous[1][0]
            remaining = previous[1][1:]
            if history[-2] == 'R':
                d = previous[1][0] - previous[2]
            else:
                # 左行ってから右だから0を飛び越える場合
                d = L - (previous[2] - previous[1][0])
        else:
            selected = previous[1][-1]
            remaining = previous[1][:-1]
            if history[-2] == 'R':
                # 右行ってから左の0飛び越えるパターン
                d = L - (previous[1][-1] - previous[2])
            else:
                d = previous[2] - previous[1][-1]
        histories[history] = [previous[0] + d, remaining, selected]

        if len(history) == N:
            results.append(histories[history][0])
            return
        
    dfs(history + 'R')
    dfs(history + 'L')
    #  dfs(count + 1, directions, current_sum, history)

    #  if count == N:
    #      # ここでようやく距離を計算
    #      result = 0
    #      options = [_ for _ in X]
    #      if directions[0] == 0:
    #          current_position = 0
    #      else:
    #          current_position = 10
    #      for direction in directions:
    #          if direction == 0:
    #              # 時計回り
    #              new_position = options.pop(0)
    #              if new_position < current_position:
    #                  result += L - (current_position - new_position)
    #              else:
    #                  result += new_position - current_position
    #          else:
    #              # 反時計回り
    #              new_position = options.pop()
    #              # 周長から時計回りの長さを引く
    #              if new_position > current_position:
    #                  result += L - (new_position - current_position)
    #              else:
    #                  result += current_position - new_position
    #          current_position = new_position
    #      #  print(result)
    #      results.append(result)
    #      return
    #  # 0が時計で1が反時計
    #  dfs(count + 1, directions + [0])
    #  dfs(count + 1, directions + [1])

dfs('R')
dfs('L')
#  pprint(histories)
print(max(results))
