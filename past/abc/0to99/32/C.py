import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
sys.setrecursionlimit(10**7)
from queue import PriorityQueue
from fractions import gcd
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
S = [_I() for _ in range(N)]

'''
0を含むのがだるい
'''

if 0 in S:
    # 0ある場合
    print(N)
    exit()
else:
    if K == 0:
        print(0)
        exit()

right = 0
left = 0
current_value = S[0]
current_length = 0
max_length = 0
while True:
    #  print('right', right, 'left', left, 'current', current_length, 'max', max_length, 'current_value', current_value)
    if right == N-1 and left == N-1:
        if S[-1] <= K:
            max_length = max(max_length, 1)
        break
    if current_value <= K:
        # 条件満たす
        left += 1
        current_length += 1
        max_length = max(max_length, current_length)
        if left == N:
            break
        current_value *= S[left]
    else:
        if right < left:
            current_value /= S[right]
            right += 1
            current_length -= 1
        else:
            if left == N:
                break
            left += 1
            current_value = S[left]
            current_length = 0

print(max_length)
