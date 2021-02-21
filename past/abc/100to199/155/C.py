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


N = _I()

S = [input() for i in range(N)]
S.sort()

prev = ''
mx = 0
c = 0
mx_list = []
for s in S:
    #  print('s', s, prev, mx, c)
    if s == prev:
        # 連続
        c += 1
        if c > mx:
            # 最大値更新
            mx_list = [s]
            mx = c
        elif c == mx:
            # 最大値に並んだ場合
            mx_list.append(s)
    else:
        # 文字が変わった時
        if mx == 0:
            # 最初のみの条件
            mx_list = [s]
            mx = 1
        else:
            # 最大が1の場合は追加
            if mx == 1:
                mx_list.append(s)
            # カウントを初期化
        c = 1
        prev = s
for i in mx_list:
    print(i)
