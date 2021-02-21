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

"""
A * B + C = N

1 <= C <= N - 1
1 <= A,B <=N - 1

Cを固定するのは悪手
Aを固定する
BはA*B<= N-1であればなんでもいい、Cはなんでもいいため
そうすると、各Aの値に対して、N-1/A個のBの可能性がある。
それらを全て足すだけ

"""

ans = 0
for i in range(1, N):
    div = (N-1)//i
    ans += div
print(ans)
