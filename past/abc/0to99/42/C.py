import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools,pdb
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

N, K = LI()
D = LI()
nums = [i for i in range(0, 10) if i not in D]

"""
使える数字の中で一番低いものから試していく
見つかったら各桁試していく

"""
N = str(N)
ans = []
is_done = False
for n in N:
    if is_done:
        break
    for num in nums:
        if int(n) <= num:
            # このnumを使用する
            ans.append(num)
            break
    else:
        # 超える数字がなかった
        ans = [n + 1, nums[0], nums[0], nums[0], nums[0]]
        is_done = True

for a in ans:
    print(a, end = '')
