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


def main():
    L = I()
    A = []
    for i in range(1, L+1):
        A.append(I())

    print(A)

    # 最大値のindexを求める
    max_idx = A[max(A)]
    print(max_idx)
    # maxの島を特定
    last_zero_idx = 0
    start_idx = None
    end_idx = 0
    for idx, i in enumerate(A):
        if i == 0:
            if i > max_idx:
                end_idx = idx
                start_idx = last_zero_idx+1
            else:
                last_zero_idx = idx
    else:
        if start_idx is None:
            start_idx = 0
        end_idx = len(A) - 1

    print('島', A[start_idx:end_idx])

    #  # スタート地点を回す
    #  for idx, a in enumerate(A):
    #      print(idx, a)
    #      # 点idxからスタートする
    #      if idx == 0:
    #          # 前しか進めない




main()
