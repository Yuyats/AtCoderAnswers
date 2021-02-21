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
AB = [LI() for i in range(N)]
#  print(AB)

"""
左の合計と右の合計で左<右となる最小の町の数。
取った場合のインパクトの大きさ=左＋右
取らなかった場合のインパクトの大きさ
例えば、1 100の町があるとき、とったら101の差、とらなかったら-1の差となる
取った場合
高橋a+b
青木0
つまり差はa+b
取らなかった場合
高橋0
青木a
つまり差はa
同じ100の町があったとしても
1 99
と
99 1では優先度が違う
どちらかをとるなら
a+bを比べる。同じ
ではaを比べると、2つ目が大きいので差がついてしまう
1つ目を選ぶべき

候補が複数ある場合は、一番ダメージが少ないものを選ぶ
例えば、あと2つってときに、
a と a+bを比べる
A_sumからaまたはa+bの大きい方を引く
"""

AB.sort(key=lambda x: (2*x[0] + x[1]), reverse=True)
#  print(AB)

ans = 0
A_sum = sum([i[0] for i in AB])
B_sum = 0
for ab in AB:
    if A_sum < B_sum:
        break
    ans += 1
    A_sum -= ab[0]
    B_sum += ab[0] + ab[1]

print(ans)
