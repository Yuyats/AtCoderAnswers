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

W, H, x, y = LI()

'''
どこの点が与えられても、縦、横、四隅の点とむすんで面積を確認する
対角で面積が同じ場合は、2分割を意味する
正方形の場合、絶対半分にでき、原点の場合は複数個線を作れる

長方形の場合、原点の場合は複数個可能で、それ以外の場合は無理
'''

if W == H:
    # 正方形の場合
    print(W*H/2, end=' ')
    if x == y == W/2:
        print(1)
    else:
        print(0)
else:
    # 正方形以外の場合
    if x == W/2 and y == H/2:
        print(W*H/2, 1)
    else:
        #  # 中途半端な位置の点のばあい
        #  # 4隅と縦横を調査
        #  S = W*H
        #  # 縦の場合
        #  s1 = x*H
        #  s2 = S - s1
        #  sm = min(s1, s2)

        #  # 横の場合
        #  s1 = W*y
        #  s2 = S - s1
        #  sm = max(sm, min(s1, s2))
        #  print(sm, 0)

        # どんなところからでも二等分可能
        print(W*H/2, 0)
