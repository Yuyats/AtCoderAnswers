import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
sys.setrecursionlimit(10**7)
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(input())
def pf(s): return print(s, flush=True)


N = I()
b = LI()

result = []
while True:
    #  print(b)
    for i in range(1, len(b)+1):
        #  print(i)
        if b[-i] == len(b)-i+1:
            #  print('break')
            result.append(b[-i])
            b.pop(-i)
            break
    else:
        if not b:
            break
        print(-1)
        exit()
for i in result[::-1]:
    print(i)




"""
なぜ追加していくのでは解けないのか？
追加していくとすると、

"""
