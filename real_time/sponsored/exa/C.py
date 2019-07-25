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

#  N, Q = LI()
#  s = input()
#  TD = []
#  for i in range(Q):
#      TD.append(LS())

N, Q = 10**5, 10**5
s = ''.join([random.choice(string.ascii_letters) for i in range(N)])
TD = []
for i in range(Q):
    if i % 2 == 0:
        TD.append(['a','L'])
    else:
        TD.append(['b','R'])
golems = [[None]] + [[i] for i in range(N)] + [[None]]

# 各文字の位置をdictに入れる？
d = {}
for idx, char in enumerate(s):
    if d.get(char):
        d[char].append(idx)
    else:
        d[char] = [idx]
#  print(d)

#  for td in TD:
done_golems = []
for golem_idx in range(len(golems)):
    print(golem_idx)
    if golem_idx in done_golems:
        continue
    dropped = False
    for td in TD:
        if dropped:
            break
        idx_list = d.get(td[0])
        if not idx_list:
            continue
        for idx in idx_list:
            moving_golems = golems[idx+1]
            if td[1] == "L":
                golems[idx] += moving_golems
                golems[idx+1] = []
                if idx == 0:
                    done_golems += golems[idx]
                    dropped = True
                    break
            else:
                golems[idx+2] += moving_golems
                golems[idx+1] = []
                if idx == N:
                    done_golems += golems[idx+2]
                    dropped = True
                    break



#  for td in TD:
#      #  pf(td)
#      # 動く位置
#      idx_list = d.get(td[0])
#      if not idx_list:
#          continue
#      #  print(idx_list)
#      for idx in idx_list:
#      #  print('golems',golems)
#  #  print(golems)
#  print(sum(golems[1:-1]))
