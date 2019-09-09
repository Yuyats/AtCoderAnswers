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
    #  N, K = LI()
    #  X = LI()
    N = 10**5
    K = 10**5
    X1 = [-10**8 + i for i in range(10**5//2)]
    X2 = [10**8 - i for i in range(10**5//2)]
    X = X1 + X2[::-1]
    print(X)

    if K == 1 and X == [0]:
        print(0)
        return

    if 0 in X:
        X.remove(0)
        K -= 1
        N -= 1

    if min(X) > 0:
        # 右側しか見ない
        print(max(X[:K]))
        return

    if max(X) < 0:
        # 左側しかみない
        print(abs(min(X[-K:])))
        return

    left_part = []
    right_part = []
    for i in X:
        if i < 0:
            left_part.append(abs(i))
        else:
            right_part.append(i)

    left_part = left_part[::-1][:K]
    right_part = right_part[:K]

    result = 10**8


    lidx, ridx = 0, K-1
    for i in range(0, min(len(left_part), K)):
        print(i)
        #  left = d(left_part[:i], 0, 0)
        print(len(left_part[:i]) + len(right_part[:K-i]) != K)
        if len(left_part[:i]) + len(right_part[:K-i]) != K:
            continue
        if len(left_part[:i]) == 0:
            left_distance = 0
        else:
            left_distance = left_part[:i][-1]
        #  right = d(right_part[:K-i], 0, 0)
        if len(right_part[:K-i]) == 0:
            right_distance = 0
        else:
            right_distance = right_part[:K-i][-1]
        #  print('i, left, right', i, left, right)
        #  print('i, left, right', i, left_distance, right_distance)
        #  first = min(left, right)
        #  second = max(left, right)
        #  first = min(left_distance, right_distance)
        #  second = max(left_distance, right_distance)
        #  result = min(result, first*2+second)
        if left_part[lidx] < right_part[ridx]:
            result = min(result, left_part[lidx] * 2 + right_part[ridx])
        else:
            result = min(result, left_part[lidx] + right_part[ridx] * 2)
        #  result = min(result, first*2+second)
        #  result = min(result, )
        lidx += 1
        ridx -= 1

    print(result)


#  def d(arr, s, current_idx):
#      if len(arr) == 0:
#          return 0
#      if len(arr) == 1:
#          return arr[0]

#      print(arr, s)

#      if current_idx == 0:
#          s += arr[0]
#          return d(arr, s, current_idx + 1)

#      if current_idx == len(arr) - 1:
#          return s + arr[current_idx] - arr[current_idx - 1]

#      s += arr[current_idx] - arr[current_idx - 1]
#      return d(arr, s, current_idx + 1)

if __name__ == "__main__":
    main()
