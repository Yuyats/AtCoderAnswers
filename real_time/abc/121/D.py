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
def S(): return input()
def pf(s): return print(s, flush=True)


A, B = LI()
# 上から4つまででいい
# 0,3,7,11の順に0になるから。
# じゃあ最大の0は今どこなのか？
if B % 4 == 0:
    # 0になるのが1つ前
    pass
elif B % 4 == 1:
    # 0 になるのが2つ前
    B = B^(B-1)
elif B % 4 == 2:
    # 0になるのが３つ前
    B = B^(B-1)^(B-2)
elif B%4 == 3:
    #  B = B^(B-1)^(B-3)^(B-4)
    B = 0
    
A = A - 1
if A % 4 == 0:
    pass
elif A % 4 == 1:
    A = A ^ (A-1)
elif A % 4 == 2:
    A = A ^ (A - 1) ^ (A - 2)
else:
    #  A = A ^ (A - 1) ^ (A - 2) ^ (A - 3)
    A = 0

#  print(A,B)
print(A^B)
#  print(functools.reduce(lambda i, j: int(i) ^ int(j), AB))
