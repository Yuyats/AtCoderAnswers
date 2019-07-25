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


from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

from math import factorial
#  a = factorial(n) / factorial(r) / factorial(n - r)


N, M = LI()

bridges = []
for i in range(M):
    a, b = LI()
    bridges.append([a,b])


#  print(bridges)

# 端のつなぎ方は、すべてでNC2通りある
# 孤島になったら不便になる

for i in range(1, M+1):
    inconvinience = 0
    #  print(i)
    tmp_bridges = bridges[i:]
    #  groups = [[] for _ in range(N)]
    groups = []
    count = 0
    while tmp_bridges:
        # i番目の橋を落とすときの不便さ
        # 渡れるかどうかの判定をしたい
        # Nこのノードがある、M個のリンクがある。グループは何個あるかという話
        groups.append([tmp_bridges[0][0]])
        #  groups[count].append(tmp_bridges[0][0])
        groups[count].append(tmp_bridges[0][1])
        while True:
            if not tmp_bridges:
                break
            new_bridges = [bridge for bridge in tmp_bridges if bridge[0] in groups[count] or bridge[1] in groups[count]]
            #  print('new_bridges', new_bridges)
            if not new_bridges:
                break
            tmp_bridges = [bridge for bridge in tmp_bridges if bridge[0] not in groups[count] and bridge[1] not in groups[count]]
            #  print('tmp', tmp_bridges)
            for new_bridge in new_bridges:
                if new_bridge[0] not in groups[count]: groups[count].append(new_bridge[0])
                if new_bridge[1] not in groups[count]: groups[count].append(new_bridge[1])
        count += 1

    #  print(groups)
    # not included islands
    flatten_groups = list(itertools.chain.from_iterable(groups))
    #  print('flatten', flatten_groups)
    kotos = list(set([island for island in range(1, N+1) if island not in flatten_groups]))
    #  print('kotos', kotos)
    groups_count = len(kotos) + len(groups)
    #  print('groups_count', groups_count)
    # 孤島はすべての島と比べる通りなのでkotosC2
    if len(kotos) >= 1:
        #  print('len koto/ len gro', len(kotos), len(flatten_groups))
        inconvinience += len(kotos)*len(flatten_groups)
        if len(kotos) >= 2:
            inconvinience += len(list(itertools.combinations(range(len(kotos)), 2)))
            #  inconvinience += factorial(len(kotos)) / factorial(2) / factorial(len(kotos) - 2)
        #  inconvinience += factorial(groups_count) / factorial(2) / factorial(groups_count - 2)
    #  inconvinience += cmb(groups_count, 2)
    #  print('totyu', inconvinience)
    for i in range(len(groups)):
        for j in range(i, len(groups)):
            if i < j:
                inconvinience += len(groups[i]) * len(groups[j])
    print(inconvinience)




# 逆からやればいけるのでは？
base_inconvinience = len(list(itertools.combinations(range(N), 2)))
print('base', base_inconvinience)
groups = []
for i in range(1, M+1):
    # 逆からやっていってグループを増やしていく
    groups.append(bridges[-i][0])
    groups.append(bridges[-i][1])
    print(groups)
    inconvinience = base_inconvinience - len(groups)
