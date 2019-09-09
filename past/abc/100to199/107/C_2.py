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
        count += 1
    min_x = min(X)
    start_point = 0
    if min_x < 0:
        X = [x - min_x for x in X]
        # 左行ってから右
        start_point = -min_x

    right_items = []
    left_items = []
    for idx, i in enumerate(X):
        if i < start_point:
            left_items.append(i)
        else:
            right_items.append(i)
    left_items = left_items[-K:]
    right_items = right_items[:K]
    print(left_items, right_items)
 

    count_turn(0, 0, 0, 0)
    print(min(results))



def count_turn(t, left_sum, right_sum, count):
    global results
    global right_items, left_items, start_point
    print(t)
    # tはturning point
    if t == 0:
        for i in range(1, len(left_items)+1):
            if i == 1:
                left_sum += start_point - left_items[-i]
            else:
                left_sum += left_items[-i+1] - left_items[-i]
        if len(left_items) == K:
            results.append(left_sum)
        for i in range(0, len(right_items)):
            if i == 0:
                right_sum += right_items[i] - start_point
            else:
                right_sum += right_items[i] - right_items[i-1]
        if len(right_items) == K:
            results.append(right_sum)
        count_turn(1, right_sum, left_sum)
        return

    if t <= len(left_items) and t <= len(right_items):
        if t == 1:
            left_sum += (start_point - left_items[-t])*2 - (right_items[-t] - right_items[-t-1])
        else:
            left_sum += (left_items[-t+1] - left_items[-t])*2
            print(left_sum)
            if t < len(right_items):
                left_sum -= (right_items[-t+1] - right_items[-t])
            else:
                left_sum -= (right_items[-t] - start_point)
        results.append(left_sum)

    if t <= len(left_items) and t <= len(right_items):
        if t == 1:
            right_sum += (right_items[t - 1] - start_point)*2 - (left_items[t] - left_items[t-1])
        else:
            right_sum += (right_items[t - 1] - right_items[t-2])*2
            if t == len(left_items):
                right_sum -= (start_point - left_items[t-1])
            else:
                right_sum -= (left_items[t] - left_items[t-1])
        results.append(right_sum)
    print(results)

    if t < len(left_items) and t < len(right_items):
        count_turn(t+1, left_sum, right_sum)



if __name__ == "__main__":
    main()
