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
#  T, D = [], []
#  for i in range(Q):
#      t,d = LS()
#      TD.append([t,d])


N, Q = 10**5, 10**5
s = ''.join([random.choice(string.ascii_letters) for i in range(N)])
TD = []
T, D = [], []
for i in range(Q):
    if i % 2 == 0:
        TD.append(['a','L'])
        T.append('a')
        D.append('L')
    else:
        TD.append(['b','R'])
        T.append('b')
        D.append('R')

"""
消滅したかゴーレムひとつずつみていく
ゴレが左に落ちる＝その左のやつは全員落ちてる
ゴレが右に落ちる=その右のやつは全員落ちてる
ちなみに通った経路にいたやつも落ちてる
呪文ごとに考えると？
A->B->C
Aがくるとなしかどうか判定しなあかん
# 同じ字が連続するのは意味ない？
1匹のゴーレムが単純に落ちたかどうかだけ判定するなら、最大10**5*2計算すれば分かる
落ちたら、その右か左を全部消去
"""

d = {}
for idx, char in enumerate(s):
    if d.get(char):
        d[char].append(idx)
    else:
        d[char] = [idx]

golems = [1 for i in range(N)]
left_border = -1
for golem_idx in range(N):
    print(golem_idx)
    originl_golem_idx = golem_idx
    if s[golem_idx] not in T:
        # そもそもそこから動く術がないのでこのゴーレムは落ちない
        left_border = golem_idx
        continue
    # 落とせるかの判定
    for td in TD:
        if td[0] == s[golem_idx]:
            if td[1] == "L":
                golem_idx -= 1
            else:
                golem_idx += 1

            if golem_idx == -1:
                break
            elif golem_idx == N:
                # その右側のゴーレムは探索しない
                print(N - (left_border+1) - (N-original_golem_idx))
                exit()
    else:
        if golem_idx not in [-1,N]:
            # 落ちなかったのでそれ以降左に落ちることはない
            if not left_border:
                left_border = original_golem_idx
            
# 左に落ちないやつを探す
first_survived = -1
next_idx = 0
for golem_idx in range(N):
    original_golem_idx = golem_idx
    if s[golem_idx] not in T:
        # 落ちない
        first_survived = original_golem_idx
        break
    for td in TD:
        if td[0] == s[golem_idx]:
            if td[1] == "L":
                golem_idx -= 1
            else:
                golem_idx += 1

            if golem_idx == -1:
                # 落ちたので続ける
                break

            if golem_idx == N:
                # 右に落ちてもた
                print(golem_idx+1)
                exit()
    else:
        # 左に落ちなかった
        # 探索を終了
        first_survived = original_golem_idx
        break


right_survived = N
for golem_idx in reversed(range(first_survived+1, N)):
    # 右に落ちるか調べる
    original_golem_idx = golem_idx
    if s[golem_idx] not in T:
        # 落ちない
        print(N - (first_survived))
        


#  #  print(d)
#  for td in TD:
#      #  print('td', td)
#      if not d.get(td[0]):
#          continue
#      if td[1] == "L":
#          # 左にいくので、左からみる
#          for place_idx in d.get(td[0]):
#              #  print('pidx', place_idx)
#              if td[1] == "L":
#                  if place_idx != 0:
#                      golems[place_idx-1] += golems[place_idx]
#                  golems[place_idx] = 0
#              else:
#                  if place_idx != N-1:
#                      #  print('passing', place_idx)
#                      golems[place_idx+1] += golems[place_idx]
#                      #  print('after passing', golems)
#                  golems[place_idx] = 0
#      else:
#          # 右に行くので、右からみる
#          for place_idx in reversed(d.get(td[0])):
#              #  print('pidx', place_idx)
#              if td[1] == "L":
#                  if place_idx != 0:
#                      golems[place_idx-1] += golems[place_idx]
#                  golems[place_idx] = 0
#              else:
#                  if place_idx != N-1:
#                      golems[place_idx+1] += golems[place_idx]
#                  golems[place_idx] = 0
#      print('gol', golems)
#  print(sum(golems))

#  memo = {}

#  done_golems = []
#  for golem in range(N):
#      if golem in done_golems:
#          continue
#      # 右に落ちたか左に落ちたか判定
#      makikomi = []
#      for td in TD:
#          if td[0] == 'L':
#              golem -= 1
#          else:
#              golem += 1
#          makikomi.append(golem)
#          if golem == -1 or golem == N:
#              #消滅
#              done_golems += makikomi
#              break
#  done_golems = set([i for i in done_golems if i not in [-1, N]])
#  print(N - len(done_golems))
