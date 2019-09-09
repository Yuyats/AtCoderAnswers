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

S = input()

if len(set(S)) == 0:
    print(0)
    exit()


"""
WWBBBWBBBBW

右から行くと、4
左から行くと、4

どちらからいってもおなじか？

WBWBWBWBWB
右から->9
左から->9
どちらからいってもかわらない？

右左両方から行く場合
WWBBBWBBBBW
WWBBBBWBW

WB, BWの数を数える？

"""
ans = 0

ans += S.count("WB")
ans += S.count("BW")

print(ans)
