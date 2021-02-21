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


N, M = LI()
SC = [LI() for i in range(M)]
SC = list(set([tuple(i) for i in SC]))


"""
ちょうどN桁
特定の桁の数字が指定されている
"""
if N == 1 and M == 0:
    print(0)
    exit()

if (1, 0) in SC:
    if N == 1:
        if all(i == (1, 0) for i in SC):
            print(0)
            exit()
    print(-1)
    exit()

# 同じ桁で違う数字が指定されている場合、-1
duplicate_check_dict = {}
for s, c in SC:
    if s in duplicate_check_dict:
        if duplicate_check_dict[s] != c:
            print(-1)
            exit()
    else:
        duplicate_check_dict[s] = str(c)


SC.sort()
#  print(SC)
ans = ''
for i in range(N):
    if i == 0:
        if i + 1 in duplicate_check_dict:
            ans += duplicate_check_dict[i+1]
        else:
            ans += '1'
    elif i + 1 in duplicate_check_dict:
        ans += duplicate_check_dict[i+1]
    else:
        ans += '0'
print(ans)
