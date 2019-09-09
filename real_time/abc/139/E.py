import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools, os, pdb
sys.setrecursionlimit(10**7)
from fractions import Fraction
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
def perr(s): return print(s, file=sys.stderr)

def main():
    A_list = []
    if 'LOCAL' in os.environ:
        N = 1000
        for i in range(N):
            tmp = [j for j in range(N) if i != j]
            random.shuffle(tmp)
            A_list.append(tmp)

    else:
        N = _I()
        A_list = [LI() for i in range(N)]
        #  for i in range(N):
        #      A_list.append(LI())
        #  perr(A_list)
    new_A_list = {}
    for aidx in range(N):
        new_A_list[aidx] = tuple(i-1 for i in A_list[aidx])
    A_list = new_A_list

    """
    まず、N=1000までなので、
    1000*1000=10**6まである。
    試合の日数を最小かする。
    つまりできるだけ効率よく1日に試合を詰め込むことを考える
    そもそも1のところに2とあったら、
    全通りを求めると？
    どの試合にするかで1000*999/2の階乗=10**6/2の階乗通りある
    まず選手iの1つ目を見ていく
    その相手のところをみて、current_idxがiだったら試合可能

    """

    current_opponent_idx = None
    current_day = 0
    is_ok = False
    # 各選手の試合状況
    current_position_list = {i:0 for i in range(N)}
    done_player_list = {}
    position_sum = 0
    done_sum = (N-1)*N
    #  all_done_players = set()
    N_1 = N - 1
    for _ in range(10**7):
        #  print('day: ', current_day)
        #  print('current position list', current_position_list)
        #  pdb.set_trace()
        is_ok = False
        #  if all(position == N-1 for position in current_position_list):
        if position_sum == done_sum:
            # 全試合終了
            break

        for i in range(N_1):
            #  print('--- in for---- current position list', current_position_list)
            # 選手iが試合できるか見る
            if done_player_list.get(i):
                continue

            #  if i in all_done_players:
            if current_position_list.get(i) == N_1:
                # この選手はすべての試合を終了している
                continue

            # iの試合相手のidx
            opponent_idx = A_list.get(i)[current_position_list.get(i)]
            if opponent_idx < i:
                continue
            if done_player_list.get(opponent_idx):
                # 試合相手がすでに今日試合してた場合
                continue

            #  print('i', i)
            #  print('opponent', opponent_idx)

            # iの試合相手の次の相手が選手iなら成立する
            if A_list.get(opponent_idx)[current_position_list.get(opponent_idx)] == i:
                #  print('試合した', i, opponent_idx)
                # 試合可能
                #  done_player_list.extend([i, opponent_idx])
                #  done_player_list += (opponent_idx, i)
                #  done_player_list[i] = True
                #  done_player_list.add(opponent_idx)
                done_player_list[opponent_idx] = True
                current_position_list[i] += 1
                current_position_list[opponent_idx] += 1
                #  if current_position_list[i] == N-1:
                #      all_done_players.add(i)
                #  if current_position_list[opponent_idx] == N-1:
                #      all_done_players.add(opponent_idx)
                position_sum += 2
                # 試合がまだ可能であるというフラグをつける
                is_ok = True

        if not is_ok:
            # 1試合も成立しなかったらストップする
            print(-1)
            exit()

        done_player_list = {}
        current_day += 1

    print(current_day)
if __name__ == '__main__':
    main()
