import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools, os, pdb
sys.setrecursionlimit(10**7)
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
def perr(s): return print(s, file=sys.stderr)

S = input()
T = input()

if any(i not in sorted(list(set(S))) for i in sorted(list(set(T)))):
    print(-1)
    exit()

d = {}
for sidx, s in enumerate(S):
    if s not in d.keys():
        d[s] = []
    d[s].append(sidx+1)

if 'LOCAL' in os.environ:
    print('d', d)
current_idx = -1
round_count = 0
for tidx, t in enumerate(T):
    #  pdb.set_trace()
    if 'LOCAL' in os.environ:
        print('t:  ', t, tidx)

    char_position_idx = bisect.bisect_right(d[t], current_idx)
    if char_position_idx >= len(d[t]):
        # 同じ文字だがこえているので次の順目に
        round_count += 1
        current_idx = d[t][0]
        continue

    #  print('char posi idx', char_position_idx)
    #  print('d[t][char posi idx]', d[t][char_position_idx], current_idx)
    if d[t][char_position_idx] < current_idx:
        # この順目にない場合
        current_idx = d[t][0]
        round_count += 1
    else:
        # この順目にある場合
        current_idx = d[t][char_position_idx]
print(len(S)*round_count + current_idx)
