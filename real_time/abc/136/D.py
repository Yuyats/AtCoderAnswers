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

def main(S):
    """
    RLの組み合わせに着目
    そうすれば、自ずと最後にいる場所が分かる
    """
    # Lを探している場合はTrue
    is_L_search = True
    cur = 0
    ans = [0 for _ in range(len(S))]
    while True:
        #  print(cur, ans)
        if is_L_search:
            Lidx = S[cur:].index('L')
            # Lのところまで全部計算
            if Lidx % 2 == 0:
                # 偶数個
                ans[cur+Lidx] += Lidx // 2
                ans[cur+Lidx-1] += Lidx // 2
            else:
                if Lidx >= 3:
                    ans[cur+Lidx] += Lidx//2

                ans[cur+Lidx-1] += Lidx // 2+1
            #  #Lのぶんを足す
            #  ans[cur+Lidx] += 1
            if cur + Lidx == len(S)-1:
                ans[-1] += 1
                # 終了
                return ans
            else:
                is_L_search = False
                cur += Lidx
        else:
            # Rを探す
            try:
                Ridx = S[cur:].index('R')
            except:
                Ridx = len(S) - cur
                if Ridx % 2 == 0:
                    ans[cur] += Ridx // 2
                    ans[cur-1] += Ridx // 2
                else:
                    if Ridx >= 3:
                        ans[cur-1] += Ridx // 2
                    ans[cur] += Ridx // 2 + 1
                return ans
                # もう残りLしかないよ。
            # Rのところまで全部計算
            if Ridx % 2 == 0:
                # 偶数個
                ans[cur] += Ridx // 2
                ans[cur-1] += Ridx // 2
            else:
                # 奇数個
                ans[cur] += Ridx // 2 + 1
                if Ridx >= 3:
                    ans[cur-1] += Ridx // 2
            is_L_search = True
            cur += Ridx


    #  # 偶奇で止まった場所の最終地点をメモる？
    #  ans = [0 for _ in range(len(S))]
    #  #  is_done_list = [False for _ in range(len(S))]
    #  next_idx = 0
    #  for i in range(len(S)):
    #      if next_idx > i:
    #          continue
    #      next_idx += 1
    #      #  if is_done_list[i]:
    #      #      continue
    #      # i番目のマスから動かす
    #      if S[i] == 'R':
    #          # Rにいるとき、最初のLまでの距離を見る。最悪で左端
    #          first_L_idx = S[i+1:].index('L')
    #          # 例えば0だったら隣にあるので、最終的に自マスに戻る
    #          if first_L_idx == 0:
    #              ans[i] += 1
    #          else:
    #              # 一旦Lマスまで移動すると考える。距離を2で割った余り。
    #              if first_L_idx % 2 == 0:
    #                  # とんでるやつらの場所はわかる。なぜなら全員Rだから
    #                  #  is_done_list[:i+first_L_idx+1] = [True for _ in range(i+first_L_idx+1)]
    #                  next_idx = i+first_L_idx+1
    #                  ans[i+first_L_idx] += first_L_idx / 2
    #                  ans[i+first_L_idx+1] += first_L_idx / 2
    #              else:
    #                  # Lに止まるパターン
    #                  next_idx = i+first_L_idx+1
    #                  ans[i+first_L_idx] += (first_L_idx + 1) / 2
    #                  ans[i+first_L_idx+1] += (first_L_idx + 1) / 2
    #      else:
    #          # Lにいるとき
    #          # 最初に出会うRをみつける
    #          first_R_idx = list(reversed(S[:i])).index('R')
    #          if first_R_idx == 0:
    #              # 左隣がR
    #              ans[i] += 1
    #          else:
    #              # 一旦Rmade移動
    #              if first_R_idx % 2 == 0:
    #                  # とんでるやつらの場所はわかる。なぜなら全員Lだから
    #                  ans[i-first_R_idx] += 1
    #              else:
    #                  ans[i-first_R_idx-1] += 1
    #      #  is_done_list[i] = True
    #  return ans


if __name__ == '__main__':
    if 'LOCAL' in os.environ:
        # ローカル実行時のみ通る処理
        # テストしたい入力を入れておく
        input_values = [
                """RRLRL""",
                """RRLLLLRLRRLL""".strip(),
                """RRRLLRLLRRRLLLLL""".strip(),
                """RRLLLRL"""
                ]
        outputs = [
               "0 1 2 1 1",
               "0 3 3 0 0 0 1 1 0 2 2 0",
               "0 0 3 2 0 2 1 0 0 0 4 4 0 0 0 0",
               ""
                ]
        for idx, input_value in enumerate(input_values):
            input_value = input_value
            #  N = int(input_value[0])
            #  A = list(map(int, input_value[1].split()))
            ans = main(input_value)
            expected_value = outputs[idx]
            print(ans,'\nexp ',  expected_value)
            #  assert ans == expected_value, 'failed: ans: {ans}, exp: {exp}'.format(ans=ans, exp=expected_value)
    else:
        S = input()
        for i in main(S):
            print(int(i), end=' ')
        #  print(main(S))


