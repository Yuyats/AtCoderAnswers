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


def main():
    global N, A, B, C, l
    N, A, B, C = LI()
    l = []
    [l.append(I()) for i in range(N)]
    l = sorted(l, reverse=True)
   #  print(N, A, B, C, l)
    flags = [False]*3
    if A in l:
        l.remove(A)
        flags[0] = True

    if B in l:
        l.remove(B)
        flags[1] = True

    if C in l:
        l.remove(C)
        flags[2] = True

    g = [A, B, C]
    for idx, f in enumerate(flags):
        if f:
            g[idx] = None
 
    g = [i for i in g if i != None]
    if len(g) == 0:
        print(0)
        return
    mp = 0
    for idx, i in enumerate(g[::-1]):
        if i < min(l):
            mp += abs(l[-1]-i)
            l = l[:-1]
            g[len(g)-1 - idx] = None
    g = [i for i in g if i != None]
    

    if len(g) == 0:
        print(mp)
        return

    combis = list(itertools.product(l, repeat=len(g) + 1))
    for i in N:

    print('combis', combis)
    return
    for idx, i in enumerate(g):
        # iの数値を目指す
        # 一番近い値を目指す
        #  print('i', i)
        #  print('rest items l', l)
        min_diff = 10**8
        min_combis = []
        for n in range(1, len(l) - len(g) + idx + 2):
            #  print('n', n)
            combis = list(itertools.combinations(l, n))
            #  print('combis', combis)
            for c in combis:
                diff = (len(c)-1) * 10 + abs(i - sum(c))
                if diff < min_diff:
                    min_diff = diff
                    min_combis = c
        #  print('min_combis', min_combis, min_diff)
        mp += min_diff
        for mc in min_combis:
            l.remove(mc)

        #  nearest = min(l, key=lambda x:abs(x-i))
        #  #  for i in range(0, len(l) - (len(g) - 1) - idx):
        #  print('nearest', nearest)
        #  if abs(i - nearest) <= 10:
        #      mp += 10
        #      l.remove(nearest)
        #      continue




    print(mp)

#  def dfs(0, s, m, target, limit):
     


def find_combi(target):
    print('target', target)
    min_diff = 10**9
    min_combi = []
    for idx, i in enumerate(l):
        for jidx, j in enumerate(l):
            if idx == jidx: continue
            if abs(target - (i + j)) < min_diff:
                min_diff = abs(target - (i+j))
                min_combi = [idx, jidx]
            print(i, j)

    print('min_combi, min_diff', min_combi, min_diff)
    i_item = l[min_combi[0]]
    j_item = l[min_combi[1]]
    l.remove(i_item)
    l.remove(j_item)
    return min_combi, min_diff



if __name__ == "__main__":
    main()
