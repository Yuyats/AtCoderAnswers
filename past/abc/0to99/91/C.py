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
def pf(s): return print(s, flush=True)

N = I()
A,B = [], []
for n in range(N):
    A.append(LI())
for n in range(N):
    B.append(LI())

#  N = 100
#  A,B = [], []
#  for n in range(N):
#      A.append([random.randint(0,2*N), random.randint(0, 2*N)])
#  for n in range(N):
#      B.append([random.randint(0,2*N), random.randint(0, 2*N)])

B = sorted(B, key=lambda x: x[0])

result = 0
for b in B:
    tmp = [a for a in A if a[0] < b[0] and a[1] < b[1]]
    if not tmp:
        continue
    result += 1
    closest = max(tmp, key=lambda x: x[1])
    A.remove(closest)
print(result)

#  """
#  一旦赤い点がどの青い点を持てるのかを洗い出す
#  lenが小さい順に青を消していく。
#  何個消せるかで勝負
#  """

#  b_a = []
#  for b in B:
#      tmp = []
#      for a in A:
#          if a[0] < b[0] and a[1] < b[1]:
#              # 赤が青より小さいとき
#              tmp.append(a)
#      if tmp:
#          b_a.append(tmp)
#  #  print(b_a)

#  result = 0
#  results = []
#  #  print('ba', b_a)
#  def dfs(arr, count):
#      print(arr)
#      #  print('count', count)
#      #  for i in range(len(arr)-1, -1, -1):
#      tmp = sorted(arr, reverse=True, key=len)
#      popped = tmp.pop(tmp.index(min(tmp, key=len)))
#      while not popped:
#          if not tmp:
#              results.append(count)
#              return
#          popped = tmp.pop(tmp.index(min(tmp, key=len)))
#      #  print('popped', popped)
#      #  tmp = [_ for _ in arr]
#      for p in popped:
#          l = [[k for k in j if k != p] for j in tmp]
#          #  l = [j for j in l if j]
#          #  print('l',l)
#          if not l:
#              results.append(count+1)
#          else:
#              dfs(l, count+1)

#  if not b_a:
#      print(0)
#      exit()
#  dfs(b_a, 0)
#  #  print(results)
#  if not results:
#      print(0)
#      exit()
#  print(max(results))


#  #  for i in range(len(b_a)-1, -1, -1):
#  #      b_a = sorted(b_a, reverse=True, key=lambda x: len(x))
#  #      popped = b_a.pop()[0]
#  #      if len(popped) >= 2:
#  #          # 全通り試したい
#  #      result += 1
#  #      #  print('popped', popped)
#  #      b_a = [[k for k in j if k != popped] for j in b_a]
#  #      b_a = [j for j in b_a if j != []]
#  #      #  print(b_a)
#  #      if not b_a:
#  #          break
#  #      #  b_a = [1:]
#  #      #  b_a[0]
#  #  print(result)
