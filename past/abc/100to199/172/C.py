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

N,M,K = LI()
A = LI()
B = LI()

A_cum = [A[0]]
[A_cum.append(A_cum[i-1] + A[i]) for i in range(1, len(A))]
print(A_cum)
print([a/(aidx+1) for aidx, a in enumerate(A_cum)])

B_cum = [B[0]]
[B_cum.append(B_cum[i-1] + B[i]) for i in range(1, len(B))]
print(B_cum)
print([b/(bidx+1) for bidx, b in enumerate(B_cum)])

A = []
for a in A_cum:
    if a > K:
        break
    else:
        A.append(a)

B = []
for b in B_cum:
    if b > K:
        break
    else:
        B.append(b)

print(A,B)


ans = 0
for aidx, a in enumerate(A):
    for bidx, b in enumerate(B):
        print(aidx, bidx)
        if a + b > K:
            ans = max(ans, aidx + bidx + 2 - 1)
            break
    else:
        ans = max(ans, aidx + bidx + 2)
print(ans)
