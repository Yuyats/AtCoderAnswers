import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
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
def I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)

S = input()
T = input()
if len(S) < len(T):
    print('UNRESTORABLE')
    exit()
result = []
for sidx, s in enumerate(S):
    #  print('sidx,s', sidx, s)
    # どこから始めるかで考える
    if sidx + len(T) > len(S):
        continue
    for tidx, t in enumerate(T):
        #  print('tidx, t', tidx, t)
        if S[sidx+tidx] == '?':
            continue
        if t != S[sidx+tidx]:
            # 一致しない場合はこれではない
            break
    else:
        # 鍵発見
        #  print('sidx', sidx)
        ans = S[:sidx] + T
        if sidx + len(T) < len(S):
            ans += S[sidx+len(T):]
        ans = ans.replace('?', 'a')
        result.append(ans)
if result:
    print(min(result))
else:
    print('UNRESTORABLE')
