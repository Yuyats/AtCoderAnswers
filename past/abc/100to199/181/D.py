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

S = input()
"""
最大で2*10**5桁
下3桁で判定可能
111-999の数字の組み合わせがlistにあるか判定
"""

if len(S) == 1:
    if int(S) % 8 == 0:
        print('Yes')
    else:
        print('No')
    exit()
elif len(S) <= 2:
    if int(S[0]+S[1]) % 8 == 0 or int(S[1] + S[0]) % 8 == 0:
        print('Yes')
    else:
        print('No')
    exit()

S = [i for i in S]

counts = collections.Counter(S)
#  print(counts)
#  import pdb
#  pdb.set_trace()
candidates = [str(i) for i in range(112, 1000, 8)]
for candidate in candidates:
    #  print(candidate)
    for l in candidate:
        if counts[l] >= candidate.count(l):
            continue
        else:
            break
    else:
        print('Yes')
        exit()
else:
    print('No')
