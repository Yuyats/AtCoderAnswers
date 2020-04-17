#  import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
#  sys.setrecursionlimit(10**7)
#  from queue import PriorityQueue
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
#  def gcd(*numbers):
#      return functools.reduce(math.gcd, numbers)
#  def make_divisors(n):
#      divisors = []
#      for i in range(1, int(n**0.5)+1):
#          if n % i == 0:
#              divisors.append(i)
#              if i != n // i:
#                  divisors.append(n//i)

#      divisors.sort(reverse=True)
#      return divisors

import gcd
K = int(input())

ans = 0
for a in range(1, K+1):
    for b in range(1, K+1):
        for c in range(1, K+1):
            ans += gcd(gcd(a,b),c)
print(ans)
exit()

d = {}
vals = []
for i in range(1, K+1):
    for j in range(1, K+1):
        nums = [i,j]
        nums.sort()
        key = str(i) + '-' + str(j)
        if key in d:
            vals.append(d[key])
        else:
            val = gcd(i,j)
            d[key] = val
            vals.append(val)
#  print(vals)
#  print(d)
for val in vals:
    for k in range(1, K+1):
        #  print(val, k)
        nums = [i,j]
        nums.sort()
        key = str(val) + '-' + str(k)
        if key in d:
            ans += d[key]
        else:
            val = gcd(val, k)
            ans += val
            d[key] = val
print(ans)
exit()
for i in range(1, K+1):
    for j in range(1, K+1):
        for k in range(1, K+1):
            nums = [i,j,k]
            nums.sort()

            key = '{}-{}-{}'.format(nums[0], nums[1], nums[2])
            if key in d:
                ans += d[key]
                continue

            min_num = nums[0]
            divisors = make_divisors(min_num)
            #  print(divisors)
            for divisor in divisors:
                #  if gcd(divisor, nums[1], nums[2]) == divisor:
                if nums[1] % divisor == 0 and nums[2] % divisor == 0:
                    d[key] = divisor
                    ans += divisor
                    break

            #  print(d)
            #  ans += val
print(ans)
