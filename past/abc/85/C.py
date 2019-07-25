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

N, Y = LI()

m = [10000, 5000, 1000]


"""
2000枚をどうふりわけるかで考える？
2000 0 0
1999 1 0
1998 2 0
的な
左端を固定、残りを右側でdfsしたら、
例えば1000なら、1000通り試せば良い
10**6ぐらいで終わるか？
"""
for i in range(N + 1):
    # i は1万円札の数
    ten = m[0] * i
    rest = N - i
    # 残りを5000/1000の振り分けを行う
    for j in range(rest + 1):
        five = m[1] * j
        one = m[2] * (rest - j)
        if ten + five + one == Y:
            print(i, j, rest - j)
            exit()
else:
    print(-1, -1, -1)
