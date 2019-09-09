import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools, os
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
def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('- {} -> {}'.format(name, val), file=sys.stderr)
            return None
"""
書き換えたあとの最大公約数の最大値を求める
書き換える値の最適解は、最小値を最大値に書き換えること
例えば、1,6,3があるとき、1を3に書き換えることで最大公約数が3になる
しかし、7 6 8の場合、最小の6ではなく7を書き換えることが最適となる
結局全部の数について書き換えたときの最大値を求めるしか無いか
そうするとO(N**2)になってしまう
全体の最大公約数はgcd(gcd(gcd(1,2), 3),4)
1つ書き換えるは、消すと同義
逆でやる？
全部のgcdを求めて、そこから途中結果を保存しておく
7 6 8 なら
None 1 1と
None 2 1
Noneと2なので2

"""
#  def main(N, A):
#      tmp = A[0]
#      tmp_list = [A[-1], A[0]]

#      for i in range(N-1):
#          tmp = fractions.gcd(tmp, A[i+1])
#          tmp_list.append(tmp)

#      tmp = A[-1]
#      reversed_tmp_list = [A[0], A[-1]]
#      for i in range(N-1):
#          tmp = fractions.gcd(tmp, A[-(i+2)])
#          reversed_tmp_list.append(tmp)

#      debug(tmp_list, locals())
#      debug(reversed_tmp_list, locals())

#      answers = []
#      for i in range(N):
#          #  if i == 0:
#          #      answers.append(reversed_tmp_list[-(i+2)])
#          #      continue
#          #  if i == N - 2:
#          #      answers.append(tmp_list[i])
#              #  continue
#          tmp = fractions.gcd(tmp_list[i], reversed_tmp_list[-(i+2)])
#          answers.append(tmp)
#      debug(answers, locals())
#      return max(answers)


#  if __name__ == "__main__":
#      if 'LOCAL' in os.environ:
#          values = [
#                  [
#                      4,
#                      [2, 4, 6, 8],
#                      2
#                      ],
#                  [
#                      2,
#                      [100000, 100000],
#                      100000
#                      ],
#                  [
#                      3,
#                      [12, 6, 12],
#                      12
#                      ],
#                  [2, [1, 1000000], 1000000],
#                  [2, [1, 1], 1],

#                  [8, list(map(int, '746130 1385670 4849845 881790 3233230 1939938 570570 510510'.split())), 19]
#                  ]
#          for i in values:
#              print('A', i[1])
#              res = main(i[0], i[1])
#              print('res: {res}, exp: {exp}'.format(res=res, exp=i[2]))
#              assert res == i[2]
#      else:
#          N = _I()
#          A = LI()
#          print(main(N, A))

import os

def main(N, A):
    # 処理を書く
    return N 


if __name__ == '__main__':
    if 'LOCAL' in os.environ:
        # ローカル実行時のみ通る処理
        # テストしたい入力を入れておく
        input_values = [
                """3
7 6 8
3
                """.strip(),
                """3
12 15 18
6
                """.strip()
                ]
        for input_value in input_values:
            input_value = input_value.split('\n')
            N = int(input_value[0])
            A = list(map(int, input_value[1].split()))
            ans = main(N, A)
            expected_value = int(input_value[2])
            assert ans == expected_value, 'failed: ans: {ans}, exp: {exp}'.format(ans=ans, exp=expected_value)
    else:
        # 実際に提出したときの処理
        N = 'some_input'
        A = 'some_input'
        print(main(N, A))

