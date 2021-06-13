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
AB = [LI() for i in range(M)]

#  AB = []
# 重複は取っておく
#  for i in range(M):
#      data = LI()
    #  if data not in AB:
    #      AB.append(data)

"""
N人
a,bは友達
a-b, b-cならa-c
例えば
a,c,b
d,e,f
g,h,i
が友達なら、3つのグループにわければいい
一番友達の繋がりが多い数を調べて、その人数分のグループを作る
a,b,c
b,d,e
g,h,i
なら
a,b,c,d,eが友達であるので5グループに分ければ良い

1つ1つ見ていって、dictに格納
x-y-z-aの場合、全員友達
"""

from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

#  friend_dict = {i: set() for i in range(1, N + 1)}
#  for a, b in AB:
#      friend_dict[a].add(b)
#      friend_dict[b].add(a)
#      friend_dict[a] = friend_dict[a].union(friend_dict[b])
#      friend_dict[b] = friend_dict[b].union(friend_dict[a])
#  #  print(friend_dict.values())
#  #  print(friend_dict, max([len(i) for i in friend_dict.values()]))

uf = UnionFind(N+1)
#  print(uf)
for a, b in AB:
    uf.union(a, b)
#  print(uf)
print(max([len(i) for i in uf.all_group_members().values()]))
#  print(max([len(i) for i in friend_dict.values()]))

