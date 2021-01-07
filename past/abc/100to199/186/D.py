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
A = LI()
"""
全ての数の組み合わせについて、それぞれの絶対値を合計する問題。
全てあげていては時間オーバーとなる
全ての組み合わせは
2*10^5C2となる=10^10
全ての数はN-1回あらわれる。
5 4 3 2なら
5-4, 5-3, 5-2
ソートしたほうがわかりやすいか？

ある数について着目
A1については、AをN-1回から他の数の合計を引く
そうすると、A1より大きい数も小さい数もでてくるため、ソートしておく。
昇順にソートすると、
A1より大きい数の合計とA1*(N-1)の絶対値をとればよい。
A2なら、A2より大きい数の合計とA2*(N-1-1)の絶対値。
これを全要素について行う
"""

N = _I()
A = LI()

# 昇順ソート
A.sort()

# ある数以上の要素の合計値
cm = []
total = sum(A)
for a in A:
    total -= a
    cm.append(total)

ans = 0
for idx, a in enumerate(A[:-1]):
    x = cm[idx] - a * (N - 1 - idx)
    ans += x
print(ans)
