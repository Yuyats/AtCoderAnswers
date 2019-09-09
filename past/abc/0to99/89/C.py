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

N = I()
S = []
for i in range(N):
    S.append(input())
#  N = 10**5
#  S = []
#  for i in range(N):
#      S.append(random.choice(string.ascii_letters))

# count?
"""
countして、かけていく
"""
M, A, R, C, H  = 0,0,0,0,0

for s in S:
    if s[0] == "M":
        M += 1
    elif s[0] == "A":
        A += 1
    elif s[0] == "R":
        R += 1
    elif s[0] == "C":
        C += 1
    elif s[0] == "H":
        H += 1

l = [M,A,R,C,H]
result = 0
for i in range(len(l)-2):
    for j in range(i+1, len(l)-1):
        for k in range(j+1, len(l)):
            result += l[i]*l[j]*l[k]
print(result)
