import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
sys.setrecursionlimit(10**7)
from queue import PriorityQueue
from fractions import gcd
inf, eps, mod = 10 ** 20, 1.0 / 10**10, 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)
def _cumsum(l): return list(itertools.accumulate(l))
H, W, A, B = LI()

"""
1000*1000=1000000=10**6なので、無理
小さい方をA,Bとする
てことは、0にするか1にするかの話
100と001は同じ
まず左上から埋めていく
小さい方ということは000なら0だし、001なら1だし、010なら1だし、011なら1だし、111なら0
つまり最大値が半分H//2, W//2
そもそもA, Bがそれらを超えているとアウト
超えていなければできる？

5 5 1 1なら
1
 1
  1
   1
    1
    5 5 2 1なら
1 1
   1 1
      1 と詰まってしまうので無理
5 5 2 2なら
11000
01100
00110
00011
10001

2 6 3 1
111000
000111

2 6 2 1
111100
000011
0のときはいつもできる
2 5 0 0
00000
00000
2 6 3 0
111000
111000

2 6 0 1
000000
111111

2 6 0 0
000000
000000

4 6 0 2
000000
111111
000000
111111

"""
ans = []
if A == 0 and B == 0:
    for h in range(H):
        tmp_s = ['0']*W
        ans.append(tmp_s)
elif A == 0 and B != 0:
    # 行がすくない法0
    for b in range(B):
        tmp_s = ['0']*W
        ans.append(tmp_s)
    for h in range(B, H):
        tmp_s = ['1']*W
        ans.append(tmp_s)
elif A != 0 and B == 0:
    for h in range(H):
        tmp_s = ['0']*A + ['1']*(W-A)
        ans.append(tmp_s)
for a in ans:
    print(a)

