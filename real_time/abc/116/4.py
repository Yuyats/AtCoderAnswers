import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
from operator import itemgetter


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
    # 種類最小から最大までそれぞれ計算する
    N, K = LI()
    T = []
    D = []
    for i in range(N):
        t, d = LI()
        T.append(t)
        D.append(d)
    #  print(T, '\n', D)
    TD = [[t, d] for t, d in zip(T, D)]
    TD = sorted(TD, key=itemgetter(1), reverse=True)
    #  print('TD', TD)

    all_types = set(T)
    results = []
    for i in range(1, K+1):
        #  print('\n---------\n',i,'回目')
        # iを種類数とみなす
        # 最小種類数のときの最大値、最大種類数のときの最大値を計算して比較する
        # 何を選んだかは関係ない
        
        # 種類の全組み合わせを求める
        #  print(i)
        combinations = list(itertools.combinations(all_types, i))
        #  print('combi', combinations)
        type_bonus = i * i
        for combination in combinations:
            #  print('\n')
            base_point = 0
            # 各組み合わせでの最大値を求める
            current_options = [i for i in TD if i[0] in combination]
            #  print('current_options: ', current_options)
            # そもそも数がKに満たない場合は作るのが不可能なため次のループへ
            if len(current_options) < K:
                continue

            required_neta_count = K
            # 各タイプの最大値をまず選び、current_optionsから排除
            for t in combination:
                #  current_options = [i for i in TD if i[0] in combination]
                max_value = max([option[1] for option in current_options if option[0] == t])
                #  print('max_value', max_value)
                base_point += max_value
                # max_valueは選択肢から取り除いておく
                current_options = [i for i in current_options if not (i[0] == t and i[1] == max_value)]
                #  print('選んだ寿司を選択肢から取り除いた', current_options)

            required_neta_count -= i
            #  print('あと何個ネタを取るべきか? ', required_neta_count, '個')
            # あとは残りの選択肢から大きいものを選ぶ
            #  print('current_options, requried_neta_count', current_options, required_neta_count)
            result = sum([i[1] for i in current_options[:required_neta_count]]) + base_point
            results.append(result + type_bonus)

    #  print('\n======================\nresults', results)
    print(max(results))


main()
