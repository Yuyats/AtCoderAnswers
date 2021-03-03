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
C = input()
C = [i for i in C]

"""
一番左にあるWを一番右にあるRと入れ替えるのは最善手
それが終われば、赤を白に変える
"""

ans = 0

if 'W' not in C or 'R' not in C:
    print(0)
    exit()

w_idx_list = []
r_idx_list = []
for idx, i in enumerate(C):
    if i == 'W':
        w_idx_list.append(idx)
    else:
        r_idx_list.append(idx)
w_idx = 0
r_idx = -1

#  print(w_idx_list, r_idx_list)
while len(w_idx_list) > w_idx and len(r_idx_list) > -r_idx-1:
    if w_idx_list[w_idx] > r_idx_list[r_idx]:
        break
    #  print(w_idx, r_idx)
    ans += 1
    w_idx += 1
    r_idx -= 1
print(ans)
