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
    if min_x < 0:
        X = [x - min_x for x in X]
        # 貪欲的にいく？
        dfs(-min_x, 0, X, 0, count)
    else:
        dfs(0, 0, X, 0, count)

    print(min(results))


def dfs(p, s, rest, pidx, count):
    global N, K, results
    # 該当のものを使うか
    # 右に行くか左に行くかの判断
    # k個選んだら終了
    if count == K:
        results.append(s)
        return

    if rest[-1] < p:
        # 右側には数字がない
        #  for idx, i in enumerate(rest):
        #      if idx > K - count - 1:
        #          results.append(s)
        #          return
        #      if idx == 0:
        #          s += 
        dfs(rest[-1], s+p-rest[-1], rest[:-1], 0, count+1)
        return

    if rest[0] > p:
        # 左側に数字がない
        # K個選んで終わり
        for idx, i in enumerate(rest):
            if idx > K - count - 1:
                results.append(s)
                return
            if idx == 0:
                s += i - p
            else:
                s += i - rest[idx-1]
        #  dfs(rest[0], s+rest[0] - p, rest[1:], 0, count+1)
        return

    if pidx == 0:
        for ridx, r in enumerate(rest):
            if r > p:
                left = rest[ridx - 1]
                new_rest = rest[:ridx-1] + rest[ridx:]
                dfs(left, s + p - left, new_rest, ridx - 1, count+1)

                right = r
                new_rest = rest[:ridx] + rest[ridx+1:]
                dfs(right, s + right - p, new_rest, ridx, count+1)
                return
    else:
        left = rest[pidx - 1]
        new_rest = rest[:pidx-1] + rest[pidx:]
        dfs(left, s+p-left, new_rest, pidx - 1, count+1)

        right = rest[pidx]
        new_rest = rest[:pidx] + rest[pidx+1:]
        dfs(right, s+right - p, new_rest, pidx, count+1)



if __name__ == "__main__":
    main()
