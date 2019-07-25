import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
import numpy as np
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


def main():
    N, M = LI()
    X = LI()
    #  print(N, M, X)

    X.sort()
    #  print(X)

    if N >= M:
        print(0)
        return
    if N == 1:
        # 端から端までの距離
        print(X[-1] - X[0])
        return

    N_position_list = []
    # 各xの差をとる
    X_diff = [X[i+1] - X[i] for i in range(len(X)-1)]
    X_diff_idx = np.argsort(X_diff)
    #  order_idx = np.argsort(X_diff)
    #  #  print(X_diff)
    #  # 最大値の両脇にコマを置く
    #  # コマが１つしかおけない場合、外側に置く
    count = 0
    torn_point = []
    
    #  while count < N - 1:
    #      torn_point.append(order_idx[-1])
    #      X_diff[order_idx[-1]] = -10**5-1
    #      order_idx = order_idx[:-1]
    #      count += 1

    while count < N -1:
        torn_point.append(X_diff_idx[-1 - count])
        count += 1


   
    #  print('torn_point', torn_point)
    # あとは移動距離の計算
    # listを分断していく
    torn_list = []
    for i in range(len(torn_point)):
        if i == 0:
            torn_list.append(X[0:torn_point[i]+1])
        else:
            torn_list.append(X[torn_point[i-1]+1:torn_point[i]+1])
    else:
        torn_list.append(X[torn_point[-1]+1:])

    #  print('torn_list', torn_list)

    move_count = 0
    for l in torn_list:
        if len(l) >= 2:
            # 端から端までを加算
            move_count += l[-1] - l[0]

    print(move_count)


main()
