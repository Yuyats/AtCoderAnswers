import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools

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


N = _I()

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ans = ''
for i in range(1, 99):
    #  print(i, N, 26**i, ans)
    if N <= 26 ** i:
        N -= 1
        #  print('-----', N, N % 26)
        # この時点でi桁の中で何番目かという問題になっている
        for j in range(i):
            #  ans += chr(ord('a') + N % 26)
            #  print('-----', j, N, N % 26)
            ans += ascii_lowercase[N % 26]
            N //= 26
        break
    else:
        N -= 26 ** i
print(ans[::-1])  # reversed


"""
26文字*26文字*といった数でどこまで割れるかを見る
a-z: 26**0-26**1
aa-zz: 26**1-26**2
aaa-zzz回=26**2-26**3
どこに属しているか判定
N/26すると
26*26/26= 26

余り
26の数だけ増えていく
余りが26*5+1なら
5回桁上り
a=26*0+1
b=26*0+2
aa=26*1 + 1
ab=26*1 + 2
az=52=26*1+26
ba=53=26*2+1
zz=702=26*26+26
aaa=703=26*26+26+1
aab=704=26*26*1+26*1+2
zzz=18278=26*26*26 + 26*26 + 26

何桁まで分かればOK
そしたら26**10
なら、

"""

#  ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

#  if N <= 26:
#      print(ascii_lowercase[N-1])
#      exit()

#  # 何桁かの区切りを格納
#  X = []
#  for i in range(0, 15):
#      if i == 0:
#          X.append(1)
#      else:
#          X.append(X[-1]+26**i)

#  print(X)

#  ans = []
#  for i in reversed(X):
#      #  print('i', i)
#      if i <= N:
#          # NはX.index(i)+1桁
#          print('桁', X.index(i)+1)
#          digits = X.index(i)
#          while True:
#              check_num = 26**(digits)
#              for j in range(26, 0, -1):
#                  print('check_num', check_num*j)
#                  exit()
#                  if N >= check_num*j:
#                      ans.append(check_num*j)
#                      N -= check_num*j
#                      digits -= 1
#                      break
#                  if N <= 26:
#                      ans.append(N)
#                      print(ans)
#                      exit()
#          break
#  exit()

#  """
#  aaa-zzz
#  111,26,26,26
#  半分は
#  1,13,26
#  a,m,z

#  2分探索ならいける？
#  3桁なら
#  18278-702=18080通りから検索すればいい
#  例えば、54番目とすると、
#  54/26=2...2
#  26/2=0...2
#  となるので、
#  22=26*2+2=54となる
#  つまり、bb
#  27=aa
#  52=az
#  53=ba
#  54=bb
#  例えば、18277番目とすると
#  18277/26=702...25
#  702/26=27...0
#  27//26=1...1
#  つまり、
#  1,0,25
#  つまり
#  z
#  """

#  results = []
#  for i in range(15, 1, -1):
#      # i桁目の場合
#      for j in range(26, 0, -1):
#          if 26**(i-1) * j <= N:
#              N -= 26**(i-1) * j
#              results.append(j)
#              break
#  else:
#      print(N)
#  print(results)

#  #      print(i)
#  #      exit()
#  #  results = []
#  #  c = 0
#  #  while N != 0:
#  #      remainder = N%26
#  #      N = N // 26
#  #      c +=kkkkk

#  #  results = list(reversed(results))
#  #  print('----', results)
#  #  #  for i in range(len(results)):
#  #  #      results[i] = ascii_lowercase[results[i]]
#  #  #  print(results)
#  #  #  results = [i for i in results if type(i) != int]
#  #  #  print(''.join(results))
