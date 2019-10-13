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
#  if K <= 5:
#      print(S*K)

if len(S) == 1:
    print(math.floor(K//2))
    exit()
if len(S) == 2:
    if S[0] == S[1]:
        print(K)
    else:
        print(0)
    exit()

if len(set(S)) == 1:
    print(math.floor(len(S) * K / 2))
    exit()

# 端変えないので、中だけ
#  previous = 'HOGE'
#  for s in S:
#      if s == previous:
#          ans += K
#          previous = 'HOGE'
#      else:
#          previous = s

# 連続する部分を抜き出して数える


original_last_char = S[-1]
if S[0] == S[-1]:
    S = S[:-1] + '?'
    ans += K - 1
    # 端は上で変えられた
else:
    pass
#  print('hashi', ans)

torn_list = []
previous = 'hoge'
for s in S:
    #  print(s)
    if s == previous:
        torn_list[-1] += 1
    else:
        torn_list.append(1)
        previous = s

#  print(torn_list)

for item in torn_list:
    if item >= 2:
        ans += math.floor(item/2)*K
#  print('torn', ans)
# last K
if S[-1] == '?':
    #  pdb.set_trace()
    last_sequence = torn_list[-2]
    ans -= math.floor(last_sequence/2)
    if original_last_char == S[-2]:
        last_sequence += 1
    if last_sequence >= 2:
        ans += math.floor(last_sequence/2)

print(ans)
