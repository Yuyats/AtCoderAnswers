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

N = _I()
XY = [LI() for i in range(N)]

"""
3点が同一直線状にあるか判定
2点から直線を求め、その式に3点目を代入して成り立てばOK

100点しかないので、161,700通りを確認する。


a, b
c, d
y = (b-d/a-c)*x + i
b = (b-d)/(a-c)*a + i
i = b - (b-d)/(a-c)*a
y = (b-d/a-c)*x + b - (b-d)/(a-c)*a
y*(a-c) = (b-d)*x + b*(a-c) - (b-d)*a
"""

def judge(A, B, C):
    #  print(A,B,C)
    if (A[0]-B[0]) == 0:
        # 傾きが0、y軸と並行
        return C[0] == A[0]
    else:
        left = C[1] * (A[0] - B[0])
        right = (A[1]-B[1])*C[0] + A[1]*(A[0] - B[0]) - (A[1]-B[1])*A[0]
        return  left == right

ans = 'No'
for i in range(0, N):
    for k in range(i+1, N):
        for j in range(k+1, N):
            if judge(XY[i], XY[k], XY[j]):
                ans = 'Yes'

print(ans)
