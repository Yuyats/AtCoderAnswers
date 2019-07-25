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

A,B,C,D = LI()

'''
cでもdでも割り切れない
逆に割り切れる数を計算する
Bまでで割り切れる個数
Aまでで割り切れる個数
B'-A'でA-Bまでの割り切れる個数が出せる
'''
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

BC = B//C
BD = B//D
BCD = B//lcm(C,D)

#  print('BC, BD, BCD', BC, BD, BCD)
B_count = B - (BC + BD - BCD)

A = A - 1
AC = A//C
AD = A//D
ACD = A//lcm(C,D)
#  print('AC, AD, ACD', AC, AD, ACD)

A_count = A - (AC + AD - ACD)

#  print(B_count, A_count)
print(B_count - A_count)
