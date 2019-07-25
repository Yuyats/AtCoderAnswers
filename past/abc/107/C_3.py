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
    global N, K, results
    global right_items, left_items, start_point
    results = []
    N, K = LI()
    X = LI()
    # すべて正にする
    if N == 1 and K == 1 and X == [0]:
        print(0)
        return

    count = 0
    if 0 in X:
        X.remove(0)
        K -= 1
        count += 1
    min_x = min(X)
    start_point = 0
    if min_x < 0:
        X = [x - min_x for x in X]
        # 左行ってから右
        start_point = -min_x

    result = 10**8
    print('X', X)
    print('start', start_point)
    # 左から順番に取る点をスライドさせていく
    for i in range(len(X)):
        print('\ni', i)
        print(X[i])
        print(X[i:i+K])
        if len(X[i:i+K]) != K:
            print('not enough')
            break
        if (X[i:i+K][-1] < start_point and X[i+K] < start_point) or (start_point < X[i:i+K][0] and start_point < X[i-1]):
            continue
        #  if not (min(X[i:i+K]) < start_point and start_point < max(X[i:i+K])):
        #      break

        print('79980', X[i:i+K])
        if start_point < X[i:i+K][0]:
            print('======09909')
            new_X = [start_point] + X[i:i+K]
            new_r = 0
            for xidx, x in enumerate(new_X):
                if xidx == 0:
                    continue
                new_r += x - new_X[xidx-1]

            result = min(new_r, result)
            print(result)
            continue

        # 左端までいって戻る場合と右端まで行って戻る場合
        # 右端と左端の距離の合計を調べて、短い方を先に行く
        left_sum, right_sum = 0, 0
        mid_point = False
        for idx, j in enumerate(X[i:i+K]):
            if j < start_point:
                print('===', X[i:i+K])
                if X[i:i+K][idx+1] > start_point:
                    if not mid_point:
                        mid_point = idx
                        left_sum += start_point - j
                        mid_point = True
                        continue
                left_sum += X[i:i+K][idx+1] - j
            else:
                if mid_point:
                    right_sum += j - start_point
                    mid_point = False
                    continue
                right_sum += j - X[i:i+K][i-1]

        first_direction = min(left_sum, right_sum)
        second_direction = max(left_sum, right_sum)
        print('f,s', first_direction, second_direction)

        result = min(first_direction*2 + second_direction, result)
        print('result', result)

    print(result)


if __name__ == "__main__":
    main()
