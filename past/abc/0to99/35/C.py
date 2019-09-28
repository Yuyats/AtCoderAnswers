import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
sys.setrecursionlimit(10**7)
from queue import PriorityQueue
from fractions import gcd
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
def _cumsum(l):
    return list(itertools.accumulate(l))

N, Q = LI()
LR = [LI() for i in range(Q)]
"""
1 1 2 3 3 4 5 5
0 1 0 1 0

1 2 3 4 4 5 7 8 8 8 9 13 18 19 20 20
1 0 1 1

l-rが白になる

ソートする？
1 4
1 5
2 5
3 3
各数字が何回出てくるか？にぶたん？
3が何回出てくるかは、始点が3以下のものを数えれば良い
終点が3以上でないとだめ


"""

ans = [0 for _ in range(N+1)]
#  print(ans)
for l, r in LR:
    ans[l-1] += 1
    ans[r] -= 1

#  print(ans)
ans = ans[:-1]
#  cumsum = _cumsum(ans)
#  cumsum = [i%2 for i in cumsum]
#  print(len(cumsum))
cumsum = [0]*(N)
cumsum[0] = ans[0]%2
for aidx in range(1, N):
    cumsum[aidx] = cumsum[aidx-1] + ans[aidx]
    cumsum[aidx] %= 2
#  print(cumsum)
for a in cumsum:
    print(a, end='')
print('')
