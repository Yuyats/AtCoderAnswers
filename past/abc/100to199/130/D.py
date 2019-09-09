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
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)

N, K = LI()
A = LI()

"""
LRを求める？
L=0, R=Nのとき、満たしているか
満たしているのであれば、LとRを動かしていく
Lの最も右のidxと、Rの最も左のidxを求める
その後、0~L, R~Nの間で組み合わせをすべて求める
L=1のとき、Rがどこまでいけるか
L=2のとき、Rがどこまでいけるか
"""
if sum(A) < K:
    # もともと満たさない場合
    print(0)
    exit()
elif sum(A) == K:
    # 減らせない
    print(1)
    exit()

ans = 0

sum_right = sum(A)
L_limit = 0
for i in range(N):
    sum_right -= A[i]
    if sum_right < K:
        L_limit = i
        break

sum_left = sum(A)
R_limit = 0
for i in range(N):
    sum_left -= A[-i-1]
    if sum_left < K:
        R_limit = i
        break

#  if L_limit == 0 and R_limit == 0:
#      print(0)
#      exit()
#  print('r_limit', R_limit)
ans += R_limit + 1
# これで右端と左端が決まった
# あとは動かしていく

# original_sumは、左端0、右端限界までいったときの左側の合計値
original_sum = sum(A[:N-R_limit])
#  print('original sum initial', original_sum)
for i in range(0, L_limit):
    #  print('i', i)
    original_sum -= A[i]
    #  print('original sum', original_sum)
    while original_sum < K:
        R_limit -= 1
        if R_limit == -1:
            # 終了
            print(ans)
            exit()
        original_sum += A[-R_limit-1]
    ans += R_limit + 1
print(ans)


