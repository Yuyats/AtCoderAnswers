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
0-9の数列
0, 9が絶対入っている
何通りあるか。

0と9を含むパターン
0を含むパターンを引くと
9を含むが0を含まないパターンが残る
同様に1を含むが0を含まないパターンを計算。
(1を含むパターン+9を含むパターン-1あり9なし-9あり1なし)/2
"""

# 全体
all_patterns_count = 10**N

# 0も9も含まないもの
no_0_no_9_count = 8 ** N

# 全体から0も9も含まないものを引いたら、0と9を含むパターンが得られる
pattern_0_9 = all_patterns_count - no_0_no_9_count

# そこから0を含むパターンを引く
pattern_0 = all_patterns_count - 9**N
pattern_9 = pattern_0

pattern_only_9 = pattern_0_9 - pattern_0
pattern_only_0 = pattern_only_9

#  print(all_patterns_count, no_0_no_9_count, '*', pattern_0_9, pattern_0, pattern_only_9)

ans = (pattern_0_9 - pattern_only_0 - pattern_only_9) % mod
print(ans)
