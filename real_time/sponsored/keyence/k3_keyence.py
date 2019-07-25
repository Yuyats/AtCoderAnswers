#  import numpy as np

#  N = input()
#  a_list = np.array(list(map(int, input().split())))
#  b_list = np.array(list(map(int, input().split())))

#  #  # すべての準備度が必要度を上回っている場合
#  #  if all([a >= b for a, b in zip(a_list, b_list)]):
#  #      print(0)
#  #  # 準備度が足りていない試験がある場合
#  #  else:
#  # そもそも準備度の総量が足りない場合
#  if sum(a_list) < sum(b_list):
#      print(-1)
#  else:
#      # 準備度を移動すれば受かる場合
#      # 一番数の大きいところから足りていないところに割り振る戦略
#      # a_listをcopy
#      a_list = [a for a in a_list]
#      # 準備度の余裕をリストに格納
#      diff_list = [c - b for c, b in zip(a_list, b_list)]
#      # 一度減算し始めたら対象が0になるまで続ける
#      selected_biggest_idx = diff_list.index(max(diff_list))
#      while not all([c >= b for c, b in zip(a_list, b_list)]):
#          if diff_list[selected_biggest_idx] == 0:
#              selected_biggest_idx = diff_list.index(max(diff_list))
#          min_idx = diff_list.index(min(diff_list))

#          # 最大と最小で移し替えを行う
#          if diff_list[selected_biggest_idx] < abs(diff_list[min_idx]):
#              # 足りていない値のほうが大きい場合
#              a_list[selected_biggest_idx] -= diff_list[selected_biggest_idx]
#              a_list[min_idx] += diff_list[selected_biggest_idx]
#          else:
#              # 足りていない値のほうが小さい場合
#              a_list[selected_biggest_idx] -= abs(diff_list[min_idx])
#              a_list[min_idx] += abs(diff_list[min_idx])
#          # diff_listを更新
#          diff_list = [c - b for c, b in zip(a_list, b_list)]
#      result_count = len([1 for a, c in zip(a_list, a_list) if a != c])
#      print(result_count)

import numpy as np

N = input()
a_list = np.array(list(map(int, input().split())))
b_list = np.array(list(map(int, input().split())))

#  # すべての準備度が必要度を上回っている場合
#  if all([a >= b for a, b in zip(a_list, b_list)]):
#      print(0)
#  # 準備度が足りていない試験がある場合
#  else:
# そもそも準備度の総量が足りない場合
if sum(a_list) < sum(b_list):
    print(-1)
else:
    # 準備度を移動すれば受かる場合
    # 一番数の大きいところから足りていないところに割り振る戦略
    # a_listをcopy
    # 準備度の余裕をリストに格納
    diff_list = a_list - b_list
    # 昇順にソート
    diff_list.sort()
    start = 0
    end = -1
    current_value = diff_list[end]
    while diff_list[start] < 0:
        # 最大値から減算
        current_value += diff_list[start]
        while current_value < 0:
            end -= 1
            current_value += diff_list[end]
        start += 1
    if start == 0:
        print(0)
    else:
        print(start - end)
        
    # 一度減算し始めたら対象が0になるまで続ける
    selected_biggest_idx = diff_list.index(max(diff_list))
    count = 0
    while not all([c >= b for c, b in zip(a_list, b_list)]):
        if diff_list[selected_biggest_idx] == 0:
            selected_biggest_idx = diff_list.index(max(diff_list))
        min_idx = diff_list.index(min(diff_list))

        # 最大と最小で移し替えを行う
        if diff_list[selected_biggest_idx] < abs(diff_list[min_idx]):
            # 足りていない値のほうが大きい場合
            a_list[selected_biggest_idx] -= diff_list[selected_biggest_idx]
            a_list[min_idx] += diff_list[selected_biggest_idx]
        else:
            # 足りていない値のほうが小さい場合
            a_list[selected_biggest_idx] -= abs(diff_list[min_idx])
            a_list[min_idx] += abs(diff_list[min_idx])
        # diff_listを更新
        diff_list = [c - b for c, b in zip(a_list, b_list)]
        count += 1
    print(count)

