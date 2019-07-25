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

D, G = LI()
PC = []
for i in range(D):
    PC.append([(i+1)*100] + LI())

PC = [tuple(i) for i in PC]

results = []
# 完答しない場合もある。
result = 0
count = 0
for i in range(PC[-1][1]):
    result += PC[-1][0]
    count += 1
    if result >= G:
        results.append(count)

for i in range(1, D+1):
    # i種類の組み合わせを選ぶ
    combis = list(itertools.combinations(PC, i))
    #  print('i, combis', i, combis)
    for combi in combis:
        # iは完答する種類数
        result = 0
        result += sum([c[0] * c[1] + c[2] for c in combi])
        count = sum([c[1] for c in combi])
        if result >= G:
            results.append(count)
            continue
        rest = [_ for _ in PC if _ not in combi]
        for r in rest[::-1]:
            for ridx in range(r[1]):
                result += r[0]
                count += 1
                if result >= G:
                    results.append(count)
print(min(results))
