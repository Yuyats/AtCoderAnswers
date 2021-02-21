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

A, B, H, M = LI()

"""
角度は分かる
60*12=720分で360度
1分が360/720=0.5度
分針
1分が6度
9時なら
9*60*0.5=270度
分針0度
270-0=270
360-270=90度

10時40分なら
10*60*0.5+40*0.5 = 300+20=320度
分針は
40*6=240度
320-240=80度
a**2 = 3**2 + 4**2 - 2*3*4*cos80度
= 9 + 16 - 24*-0.11038724383
= 9+16-4.16755626384
= 25-4.17
= 20.83
=4.564
"""

angle_A = H*60*0.5 + M*0.5
angle_B = M*6

angle = abs(angle_A - angle_B)
if angle > 180:
    angle = 360 - angle

ans = math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(math.radians(angle)))
print(ans)
