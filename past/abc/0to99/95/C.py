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

A, B, C, X, Y = LI()


"""
A+BよりもCのほうがお得な場合、XまたはYを買い切るまでCを買う
その後は、AかBで残っているものとAB*2で安い方を買う
"""
result = 0
if A+B >= C*2:
    # Cを購入する
    reduce_amount = min(X,Y)
    X -= reduce_amount
    Y -= reduce_amount
    result += C*2*reduce_amount

if X > 0:
    result += min(C*2*X, A*X)

if Y > 0:
    result += min(C*2*Y, B*Y)


print(result)
