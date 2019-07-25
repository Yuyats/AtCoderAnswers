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
    # 問題をdfs的手法で解いてみる
    N, K = LI()
    T = []
    D = []
    TD = []
    for i in range(N):
        TD.append(LI())
    TD = np.array(TD)
    # print(TD)
    TD = TD[np.argsort(TD[:, 1])[::-1]]

    neta_type_list = set([i[0] for i in TD])

    # print("neta_type, TD\n", neta_type_list, TD)
    result = 0
    for k in range(1, K+1):
        if k > len(neta_type_list):
            break
        # 1種類の場合のみ分けて考える
        if k == 1:
            result = sum([i[1] for i in TD[:K]]) + 1
            continue
        # k種類選ぶ場合を考える
        # タイプごとのカウントを保持する
        # print('\n=====k種類選ぶ場合', k, k*k)
        result = max(result, find_max_combi_value(neta_type_list, TD, k, K) + k*k)

    print(result)


def find_max_combi_value(neta_type_list, TD, k, K):
        c = 0
        type_count = [[i, 0] for i in neta_type_list]
        result = 0
        # そもそも組み合わせが作れない場合
        type_length_list = np.zeros(max([i[0] for i in TD]) + 1)
        for i in TD:
            type_length_list[i[0]] += 1
        # print(type_length_list)
        type_length_list = np.sort(type_length_list)[::-1]
        # print(type_length_list)
        if sum(type_length_list[:k]) < K:
            return 0

        while True:
            # print('\nc', c)
            # print('while type-count', type_count)
            # まず種類分確保しなくてはいけない
            # print('TD[c]\n', TD[c])
            old_type_count = copy.copy(type_count)
            # print('initial, 999909909', old_type_count, type_count)

            for idx, i in enumerate(type_count):
                try:
                    if i[0] == TD[c][0]:
                        type_count[idx][1] += 1
                except:
                    import pdb
                    pdb.set_trace()
            type_count = np.array(type_count)
            type_count = type_count[np.argsort(type_count[:, 1])[::-1]]
            result += TD[c][1]
            # i個最大のものをとって、Kに達していたら終了
            if type_count[0][1] > K - k + 1:
                # print('111111', old_type_count)
                type_count = copy.copy(old_type_count)
                result -= TD[c][1]
                # print('result0', result)
                c += 1
                continue

            # ちょうどK個選んだ場合
            # print('選んだ個数合計', sum([i[1] for i in type_count[:k]]))
            if sum([i[1] for i in type_count[:k]]) == K:
                # 0がある場合はだめ
                if any([i[1] == 0 for i in type_count[:k]]):
                    # print('======', c, type_count)
                    result -= TD[c][1]
                    type_count = copy.copy(old_type_count)
                    # print('result1', result)
                    c += 1
                    continue
                # print('end type-count\n', type_count)
                return result
            if c == len(TD)-1:
                return 0
            # print('type_count ending', type_count)
            # print('result2', result)
            old_type_count = copy.copy(type_count)
            c += 1


main()
