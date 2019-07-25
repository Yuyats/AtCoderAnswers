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
    global N, M, A, nums, costs, A_count
    N, M = LI()
    A = LI()
    A_count = [10**4 for i in A]

    nums = [1,2,3,4,5,6,7,8,9]
    costs = [2,5,5,4,5,6,3,7,6]

    print(N, M)
    print('nums', A)
    costs = [costs[i-1] for i in A]
    print('cost', costs)
    
    """
    とにかく桁を大きくしたい
    そのためには、コストの最も低いもので桁を稼ぎ、余った
    まず割り切れる数字の組を探したい

    """
    naive()


def find_pairs():
    dp = [-1 for i in range(N+1)]
    dp[0] = 0
    for i in range(M):
        #  A_count = [10**4 for i in A]
        #  print('initial A_count', A_count)
        for j in range(N + 1):
            if dp[j] >= 0:
                dp[j] = A_count[i]
            elif j < A[i] or dp[j-A[i]] <= 0:
                dp[j] = -1
            else:
                dp[j] = dp[j-A[i]] - 1
                #  A_count -= 1
        #  print('A_count', A_count)
        # 判定
        #  a_count = [10**4 - i for i in A_count]
        #  print('a_count', a_count)

    print('dp', dp)
    dp_ = [10**4 - i for i in dp]
    print('dp_', dp_)
    if dp[N] >= 0:
        print("Yes")

def naive():
    all_list = []
    for a in A:
        all_list += [a for i in range(N // a)]

    bfs(0)

    print(all_list)
    #  dp = [[0 for j in range(N+1)] for i in range(M+1)]
    #  print(dp)
    #  for i in range(M):
    #      for j in range(N):
    #          count = 0
    #          while count * A[i] < N:
    #              dp[i+1][j] = dp[i][j - count * A[i]]
    #              count += 1

    #  for i in dp:
    #      print(dp)

def bfs(i, sum):
    if num == 

main()
