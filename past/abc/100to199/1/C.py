import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools, pdb
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

Deg, Dis = LI()
Deg *= 0.1
from decimal import Decimal, ROUND_HALF_UP
speed = float(Decimal(str(Dis/60)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
S = None
#  pdb.set_trace()

#  print(speed)
if speed <= 0.2:
    print('C', 0)
    exit()
elif 0.3 <= speed <= 1.5:
    S = 1
elif 1.6 <= speed <= 3.3:
    S = 2
elif 3.4 <= speed <= 5.4:
    S = 3
elif 5.5 <= speed <= 7.9:
    S = 4
elif 8.0 <= speed <= 10.7:
    S = 5
elif 10.8 <= speed <= 13.8:
    S = 6
elif 13.9 <= speed <= 17.1:
    S = 7
elif 17.1 <= speed <= 20.7:
    S = 8
elif 20.8 <= speed <= 24.4:
    S = 9
elif 24.5 <= speed <= 28.4:
    S = 10
elif 28.5 <= speed <= 32.6:
    S = 11
elif speed >= 32.7:
    S = 12


W = None
current = 11.25
deg_ex = ['NNE', "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", 'N']
idx = 0
while True:
    if current <= Deg < current + 22.5:
        W = deg_ex[idx]
        break
    else:
        idx += 1
        current += 22.5

    if current >= 348.75:
        W = deg_ex[-1]
        break
print(W, S)
