import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools, pdb
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
"""
なかのものと端のもの
両端が一緒かどうか
一緒なら、K-1個変える
中を変える/2切り下げ
まず、端が一緒か
"""
S = input()
K = _I()
ans = 0

if len(set(S)) == 1:
    print(int(math.floor(len(S)*K/2)))
    exit()

if K >= 10:
    S = S*10
else:
    S = S*K

torn_list = []

previous = 'hoge'
for s in S:
    if previous == s:
        torn_list[-1] += 1
    else:
        previous = s
        torn_list.append(1)
print(torn_list, len(torn_list))
if K <= 9:
    for t in torn_list:
        ans += math.floor(t/2)
else:
    for t in torn_list[1:-1]:
        if t >= 2:
            ans += int(math.floor(t/2))
            print(ans)
    ans = ans / 10 * K
    # 真ん中の部分だけ計算
    print('middle', ans)

    # 端を足す
    ans += math.floor(torn_list[0]/2)
    ans += math.floor(torn_list[-1]/2)
print(int(ans))
"""
aba
5
なら
aba aba aba aba aba
端は0 0
中が
1 1 1 1で4つ
3で4つなら、100で99つ

abba
5
なら
abba abba abba abba abba
bbがK回

"""
