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
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)


S = input()

"""
10こ数字がならんでいるとして、各プラスいれるかいれないかで2**10通りある
つまり1024通りしかない
普通に計算するか、dfs
"""
def dfs(l):
    global ans
    if len(l) == len(S)-1:
        #  print(l)
        s = S[0]
        for idx, is_plus in enumerate(l):
            if is_plus:
                #  print(int(s))
                ans += int(s)
                s = S[idx+1]
            else:
                s = s + S[idx+1]
        else:
            #  print(int(s))
            ans += int(s)
    else:
        dfs(l + [True])
        dfs(l + [False])

ans = 0
dfs([])
print(ans)
