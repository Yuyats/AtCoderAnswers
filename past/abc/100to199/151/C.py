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


N, M = LI()
pS = [input().split() for i in range(M)]
#  print(pS)

d = {}
for p, S in pS:
    if p in d:
        # すでに回答済み
        if d[p]['result'] == True:
            # 正答済みなのでスキップ
            pass
        else:
            # 未正答なので処理を行う
            if S == 'AC':
                # 正答の場合
                d[p]['result'] = True
            else:
                d[p]['count'] += 1
    else:
        # 初めて回答
        d[p] = {}
        if S == 'AC':
            d[p]['result'] = True
            d[p]['count'] = 0
        else:
            d[p]['result'] = False
            d[p]['count'] = 1

ac = 0
wa = 0
for k in d.keys():
    if d[k]['result'] == True:
        ac += 1
        wa += d[k]['count']
    #  else:
    #      wa += d[k]['count']
print(ac, wa)
