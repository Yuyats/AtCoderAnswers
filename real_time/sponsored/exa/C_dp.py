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

N, Q = LI()
s = input()
TD = []
T, D = [], []
for i in range(Q):
    t,d = LS()
    TD.append([t,d])


#  N, Q = 10**5, 10**5
#  s = ''.join([random.choice(string.ascii_letters) for i in range(N)])
#  TD = []
#  T, D = [], []
#  for i in range(Q):
#      if i % 2 == 0:
#          TD.append(['a','L'])
#          T.append('a')
#          D.append('L')
#      else:
#          TD.append(['b','R'])
#          T.append('b')
#          D.append('R')


out_memo = []
stay_memo = []
result = 0
for i in range(N):
    #  print('\n', i)
    tmp_memo = []
    # 各ゴーレムがいた回数、場所を記録する
    tmp = i
    for td_idx, td in enumerate(TD):
        #  print('out_memo, stay_memo', out_memo, stay_memo)
        if [td_idx, tmp] in out_memo:
            #  print('memo out',i)
            break
        elif [td_idx, tmp] in stay_memo:
            result += 1
            #  print('memo stay',i, [td_idx, tmp], td)
            break
        #  print('---- td_idx, tmp, td', td_idx, tmp, td)
        tmp_memo.append([td_idx, tmp])

        #  print("===", s[tmp])
        if td[0] == s[tmp]:
            if td[1] == "L":
                tmp -= 1
                if tmp == -1:
                    # 消滅
                    #  print('out', tmp)
                    out_memo += tmp_memo
                    break
            elif td[1] == "R":
                tmp += 1
                #  print('tmp',tmp)
                if tmp == N:
                    #  print('消滅',i)
                    # 消滅
                    #  print('out', tmp)
                    out_memo += tmp_memo
                    break
    else:
        #  print('stay',i)
        stay_memo += tmp_memo
        result+= 1
    #  print('r', result)
print(result)
