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

C = [[0,0,0,0]]
for i in range(3):
    C.append([0] + LI())

"""
yxの順
a1 + b1 = c11
a2 + b1 = c21
a3 + b1 = c31
a1 + b2 = c12
a2 + b2 = c22

b1 = b2 + c11 - c12
b2 = -a2 + c22
b1 = -a2 + c22 + c11 - c12
a2 - a2 + c22 + c11 - c12 = c21
c22+c11 = c21 + c12

"""
#  print(C)
if (C[2][2] + C[1][1] - C[1][2] == C[2][1]) and (C[1][1] + C[3][3] == C[1][3] + C[3][1]) and (C[2][2] + C[3][3] == C[2][3] + C[3][2]):
    print("Yes")
else:
    print("No")
