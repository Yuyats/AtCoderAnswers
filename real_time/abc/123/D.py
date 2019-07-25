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

"""
最大、最大2なら、あとはなにかけあわせても最大しかない
ABCの最大2個なので、プラス残りのlen()を足す。
もし超えたら、その組み合わせで順番にもとめていく
"""
X, Y, Z, K = LI()
A = sorted(LI(), reverse=True)
B = sorted(LI(), reverse=True)
C = sorted(LI(), reverse=True)

e = []
for a in A:
    for b in B:
        e.append(a+b)
e = sorted(e, reverse=True)[:K]
results = []
for item in e:
    for c in C:
        results.append(item+c)

for i in sorted(results, reverse=True)[:K]:
    print(i)

#  #  ABC = A+B+C
#  #  ABC = sorted(ABC, reverse=True)
#  #  #  print(ABC)
#  INF = 10**18
#  a,b,c = [INF],[INF],[INF]
#  #  abc = 0
#  count = 0
#  while a[-1] > B[0] or a[-1] > C[0] or len(a) <= min(50, X):
#      a.append(A[count])
#      count += 1
#      if count >= len(A):
#          break


#  count = 0
#  while b[-1] > A[0] or b[-1] > C[0] or len(b) <= min(50, Y):
#      b.append(B[count])
#      count += 1
#      if count >= len(B):
#          break

#  count = 0
#  while c[-1] > B[0] or c[-1] > A[0] or len(c) <= min(50, Z):
#      c.append(C[count])
#      count += 1
#      if count >= len(C):
#          break
#  a = a[1:]
#  b = b[1:]
#  c = c[1:]

#  #  while a[-1] > b[0] and a[-1] > c[0] and b[-1] > a[0] and b[-1] > c[0] and c[-1] > a[0] and c[-1] > b[0]:

#  #  while not(len(a) >= min(100, X) and len(b) >= min(100, Y) and len(c) >= min(100, Z)):
#  #      if A:
#  #          if ABC[abc]in A:
#  #              a.append(ABC[abc])
#  #              A.remove(ABC[abc])
#  #      if B:
#  #          if ABC[abc]in B:
#  #              b.append(ABC[abc])
#  #              B.remove(ABC[abc])
#  #      if C:
#  #          if ABC[abc]in C:
#  #              c.append(ABC[abc])
#  #              C.remove(ABC[abc])
#  #      abc+=1
#  #  #  for abc in range(min(200, X+Y+Z)):

#  #  #      if ABC[abc]in A:
#  #  #          a.append(ABC[abc])
#  #  #          A.remove(ABC[abc])
#  #  #      if ABC[abc]in B:
#  #  #          b.append(ABC[abc])
#  #  #          B.remove(ABC[abc])
#  #  #      if ABC[abc]in C:
#  #  #          c.append(ABC[abc])
#  #  #          C.remove(ABC[abc])
#  #  #  print(a,b,c)

#  points = []
#  for i in a:
#      for j in b:
#          for k in c:
#              points.append(i+j+k)
#  #  print(points)


#  #  #  A = A[:min(250, X)]
#  #  #  B = B[:min(250, Y)]
#  #  #  C = C[:min(250, Z)]
#  #  #  # Aの中で最大の数字足すBの最大、Cの最大は全体の中で最大
#  #  #  # 3000個大きい順に求めれば良い

#  #  #  # iが決まれば、j,kのおおきさは分かる
#  #  #  BC = []
#  #  #  # 1000*1000 で10**6の計算量
#  #  #  #  for j in range(len(B)):
#  #  #  #      for k in range(len(C)):
#  #  #  #          BC.append(B[j] + C[k])

#  #  #  points = []
#  #  #  # 10**3 と 10** 6
#  #  #  #  for i in range(len(A)):
#  #  #  #      points += [bc + A[i] for bc in BC]
#  #  #  for i in range(len(A)):
#  #  #      #  for bc in BC:
#  #  #      #      points.append(A[i]+bc)
#  #  #      for j in range(len(B)):
#  #  #          for k in range(len(C)):
#  #  #              points.append(A[i] + B[j] + C[k])
#  for i in sorted(points, reverse=True)[:K]:
#      print(i)

