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
約数を求める

1,2,4,8,13
だとすると
Aが偶数の場合とBが偶数の場合
"""
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


N = 2*N
divs = make_divisors(N)

#  print(divs)
ans = 0
for div in divs:
    #  print(div, N//div)
    if div % 2 != (N//div) % 2:
        ans += 1
print(ans)
