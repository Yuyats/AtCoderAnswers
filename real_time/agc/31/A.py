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


N = I()
s = S()

inf = 10**9+7

counts = collections.Counter(s)
result = 1
for i in counts.values():
    result *= i+1
result -= 1
print(result%inf)
exit()



from math import factorial
def c(n, r):
    a = factorial(n) / factorial(r) / factorial(n - r)
    return a

count = 0
def dfs(chars, idx):
    global count
    if idx == len(s):
        count += 1
        return
    if chars == '':
        count += 1
        dfs(chars + s[idx], idx+1)
        dfs(chars, idx+1)
    else:
        if s[idx] != chars[-1]:
            count += 1
            dfs(chars + s[idx], idx+1)
        else:
            dfs(chars, idx+1)

dfs('', 0)
print(count)
exit()
result = 0
counts = collections.Counter(s)
red = [i for i in counts.values()]
tmp = 1
for i in red:
    tmp *= i
#  print('tmp', tmp)
for i in range(1, len(s)+1):
    #  print(i)
    #  import pdb
    #  pdb.set_trace()
    #  combis = list(itertools.combinations(counts, i))
    #  print('combis' ,combis)
    result += c(len(s), i)
    #  for combi in combis:
    #      #  print('combi', combi)
    #      tmp = 1
    #      for c in combi:
    #          #  print('c', c)
    #          tmp *= counts[c]
    #      #  print('tmp', tmp)
    #      result += tmp
if tmp != 1:
    for i in range(1, tmp):
        result -= c(tmp, i)
print(int(result)%inf)
