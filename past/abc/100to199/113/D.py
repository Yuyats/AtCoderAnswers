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


H, W, K = LI()
"""
場合分け
そもそもたどり着けないという場合は考慮しない

高さの分だけ左右移動できる
高さ１の場合、左右移動は１か０しかできない
高さ２の場合、左右移動は0~1までしかできない
高さ==距離の場合、場合は１つしかない
高さ>距離の場合、もどったりすることで場合がたくさんある

H, W, K = 3, 4, 1の場合
左端に棒をかけない場合、左の３本で高さ３の組み合わせを求める
左にかける、右にかける、かけないの３通り×高さ３が答え
27 = 27通り

全通り探索するのであれば、ひとつひとつの点についてループして、かけるかかけないかを選ぶ
かけるのであれば[[1,3,5], [1,2,3,5], ...]などというのをリストに入れていく
スタートして1の一番上の点をみつける
渡る
その棒の一番上の点をさぐる
渡る
を繰り返して、ゴールできればいい
"""

amidas = [[] for _ in range(W+1)]

def dfs(amida, h, w):
    #  print('h, w', h, w, amida)
    if amida is None:
        amida = [[0]*(H+1) for _ in range(W+1)]
        print('amidaaaa', amida)

    # 右端の棒まできたら下に下る
    if w >= W:
        h += 1
        w = 1

    # 高さが一番下より下ならやめる
    if h > H:
        print('end ', amida)
        #  amida[-1] = [0]*(H+1)
        a = [x[:] for x in amida]
        a[-1] = [0]*(H+1)
        amidas.append(a)
        return

    # hが今の高さで、wが今の棒の位置
    # かけた場合と、かけなかった場合を求めていく
    # 横棒をかけない場合は、右隣の棒からその右となりにかけるかを探索
    #  amida_on = copy.deepcopy(amida)

    # 横棒をかけたら、その右の右の棒からさらにその右にかけるパターンを探索
    #  amida_on[w].append(1)
    print('off h w ', h, w)
    a = [x[:] for x in amida]
    #  dfs(amida, h, w + 1)
    dfs(a, h, w + 1)
    #  amida[w][h] = 1
    a[w][h] = 1
    print('on h w ', h, w)
    a = [x[:] for x in amida]
    a[w][h] = 1
    dfs(a, h, w + 2)
    #  amida[w][-1] = 1
    #  if w+1 < W:
    #      #  amida_on[w+1].append(0)
    #      amida[w+1][-1] = 0
    #  #  print('on', h,w,amida_on)
    #  print('on h w', h, w, amida)
    #  #  dfs(amida_on, h, w + 2)
    #  dfs(amida, h, w + 2)

if W == 1:
    print(1)
    exit()
dfs(None, 1, 1)


print(amidas)
for i in amidas:
    print(i)
result = 0
for amida in amidas:
    # 上から１を探していく
    current_w = 1
    for h in range(1, H):
        print(h)
        if amida[current_w][h] == 1:
            current_w += 1
        else:
            if current_w > 1:
                # 左端でなければ、左側からかかっているかチェック
                if amida[current_w-1][h] == 1:
                    current_w -= 1

    if current_w == K:
        print('success', amida)
        result += 1


print(result)



