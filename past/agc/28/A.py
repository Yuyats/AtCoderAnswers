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
def F(): return float(sys.stdin.readline())
def pf(s): return print(s, flush=True)

N, M = LI()
s = input()
t = input()

big = max(s, t)
small = min(s, t)

for i in range(10**5):
    x = max(len(s), len(t))*i
    if x % len(s) == 0 and x % len(t) == 0:
        # 短い方の2つ目のアイテムが長い方の最後のアイテムを超えたら終了
        if (N-1)*x/N < x/M or (M-1)*x/M < x/N:
            print(-1)
            exit()

        # 割り切れるので調査
        for j in range(x):
            N_positions = [k*j/N + 1 for k in range(N)]
            M_positions = [k*j/M + 1 for k in range(M)]
            count = 0
            for N_pos, M_pos in zip(N_positions, M_positions):
                if N_pos == M_pos:
                    if s[count] != t[count]:
                        break
                count += 1
            else:
                print(x)
                exit()

