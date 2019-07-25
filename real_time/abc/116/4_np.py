import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
import numpy as np


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
    N, K = LI()
    T = []
    D = []
    TD = []
    for i in range(N):
        TD.append(LI())
    TD = np.array(TD)
    TD = TD[np.argsort(TD[:, 1])[::-1]]

    neta_type_list = set([i[0] for i in TD])
    #  max_value_per_type = [[t, max([td[1] for td in TD if td[0] == t])]for t in neta_type_list]
    #  print('max_value_per_type', max_value_per_type)
    #  content_per_type = [[t, [i[1] for i in TD if i[0] == t]] for t in neta_type_list]
    #  max_value_per_type = [[i[0], max(i[1]), np.argmax(i[1])] for i in content_per_type]
    #  content_per_type = [[i[0], [j for idx, j in enumerate(i[1]) if idx != m[2]]] for i, m in zip(content_per_type, max_value_per_type)]

    combination_list = [list(itertools.combinations(neta_type_list, idx+1)) for idx, i in enumerate(neta_type_list)]
    combination_list = list(itertools.chain.from_iterable(combination_list))

    results = [0]
    #  for combination in combination_list:
    #      type_bonus = len(combination) * len(combination)

    #      max_values = [i[1] for i in max_value_per_type if i[0] in combination]
    #      current_options = [i[1] for i in content_per_type if i[0] in combination]
    #      current_options = list(itertools.chain.from_iterable(current_options))
    #      if len(current_options) + len(max_values) < K:
    #          # そもそも不可能な組み合わせ
    #          continue
    #      elif len(current_options) + len(max_values) == K:
    #          results.append(sum(current_options) + sum(max_values) + type_bonus)
    #          continue
    #      current_options.sort(reverse=True)
    #      results.append(sum(current_options[:K-len(combination)]) + sum(max_values) + type_bonus)






    #  for i in range(1, K+1):
    #      #  print('\n---------\n',i,'回目')
    #      # iを種類数とみなす
    #      # 何を選んだかは関係ない
        
    #      # 種類の全組み合わせを求める
    #      #  print(i)
    #      if len(neta_type_list) < i:
    #          break
    #      combinations = list(itertools.combinations(neta_type_list, i))
    #      #  print('combi', combinations)
    #      type_bonus = i * i
    #      for combination in combinations:
    #          #  print('\n')
    #          # 各組み合わせでの最大値を求める
    #          current_options = [i for i in TD if i[0] in combination]
    #          #  if len([i[1] for i in content_per_type if i[0] in combination])
    #          #  print('current_options: ', current_options)
    #          # そもそも数がKに満たない場合は作るのが不可能なため次のループへ
    #          if len(current_options) < K:
    #              continue

    #          max_values = [i[1] for i in max_value_per_type if i[0] in combination]
    #          current_options = [i[1] for i in content_per_type if i[0] in combination]
    #          current_options = list(itertools.chain.from_iterable(current_options))
    #          current_options.sort(reverse=True)
    #          #  print('最大値だけとった', base_point)
    #          #  print('残りの選択肢', current_options)
    #          results.append(sum(current_options[:K-i]) + sum(max_values) + type_bonus)

    #  print('\n======================\nresults', results)
    print(max(results))


main()
