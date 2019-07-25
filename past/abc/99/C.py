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

"""
N = 6**i + 9**j
とする。

"""

N = I()

smalls = []
bigs = []
for i in range(10**5):
    small = 6**i
    big = 9**i

    if small <= N:
        smalls.append(small)
    if big <= N:
        bigs.append(big)
    if small > N:
        break

smalls = sorted(smalls, reverse=True)
bigs = sorted(bigs, reverse=True)
#  print('smalls, bigs', smalls, bigs)

result = 10**13
for i in range(0, N+1):
    #  print('i', i)
    # i は6だけで払う分
    small_n = i
    big_n = N - i

    small_idx = 0
    big_idx = 0

    small_count, big_count = 0, 0
    while small_n != 0:
        if smalls[small_idx] > small_n:
            small_idx += 1
            continue
        small_n -= smalls[small_idx]
        small_count += 1

    while big_n != 0:
        if bigs[big_idx] > big_n:
            big_idx += 1
            continue
        big_n -= bigs[big_idx]
        big_count += 1
    #  print('small_count, big_count', small_count, big_count)
    result = min(result, small_count+big_count)

print(result)





#  units = []
#  for i in range(10**5):
#      small = 6**i
#      big = 9**i

#      if small <= N:
#          units.append(small)
#      if big <= N:
#          units.append(big)
#      if small > N:
#          break

#  units = sorted(units, reverse=True)[:-2]

#  print(units)
#  results = []
#  def dfs(remainder, count, idx, idx_count):
#      #  print('r, c, idx', remainder, count, idx)
#      if idx == len(units)-1:
#          results.append(count+remainder//units[-1]+remainder%units[-1])
#          return
#      if idx == len(units):
#          results.append(count+remainder)
#          return
#      if remainder == 0:
#          results.append(count)
#          return
#      if remainder < 0:
#          return
#      if remainder < units[idx]:
#          results.append(count + remainder)
#          return
#      if idx_count == 6:
#          dfs(remainder, count, idx+1, 0)
#          return

#      dfs(remainder - units[idx], count + 1, idx, idx_count+1)
#      dfs(remainder, count, idx + 1, 0)
#  dfs(N, 0, 0, 0)
#  print(min(results))
#  exit()
#  import pdb
#  pdb.set_trace()
#  count = 0
#  while N != 0:
#      for unit in units:
#          if unit <= N:
#              if N - unit < 0:
#                  continue
#              N -= unit
#              print('n', N)
#              count += 1
#              break
#  print(count)

