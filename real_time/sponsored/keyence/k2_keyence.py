#  kchars = ['k', 'e', 'y', 'e', 'n', 'c', 'e']
#  kchars_repeat_limit = [1, 3, 1, 3, 1, 1, 3]
 
#  # 文字がそれぞれ含まれているか含まれていないかをリストに格納
#  diff_list = [char in kchars for char in S]
#  # 不要文字が含まれていた場合
#  #  if not all([char in kchars for char in S]):
#  #      # 不要文字同士が離れていた場合は不可
#  #      first_false_idx = diff_list.index(False) 
#  #      last_false_idx = diff_list.index(False)
#  #      while diff_list[first_false_idx + 1] == False:
#  #          last_false_idx += 1
#  #      else:
#  #          first_half = S[:first_false_idx]
#  #          second_half = S[last_false_idx:]
#  #          word = first_half + second_half
#  #          if word == 'keyence':
#  #              print('YES')
#  #          else:
#  #              print('NO')

#  #      # 不要文字同士がくっついていた場合は可能性を探る
#  #  elif any()
#  # 不要文字が含まれていなくてもkcharsの文字が必要以上にあらわれていた場合



S = str(input())
S = S.replace(' ', 'h')
if len(S) > 100 or len(S) < 7:
    print('NO')
elif not(S.isalpha() and S.islower()):
    print('NO')
else:
    # 分割のパターンを洗い出す方法
    k_str = 'keyence'
    patterns = [[k_str[:i], k_str[i:]] for i in range(0, len(k_str))]
    for pattern in patterns:
        if pattern[0] in S:
            next_starting_idx = S.index(pattern[0]) + len(pattern[0])
            if pattern[1] in S[next_starting_idx:]:
                print('YES')
                break
    else:
        print('NO')

#  def main():
#      S = input()
 
#      key = "keyence"
 
#      for i in range(len(key)):
#          #print(key[:i], key[i:])
#          if (S.startswith(key[:i]) and S.endswith(key[i:])):
#              return True
#      return False
#  if (main()):
#      print("YES")
#  else:
#      print("NO")


#  remaining_string = S
#  current_position = 0
#  for idx, char in enumerate(kchars):
#      if char not in remaining_string:
#          # 文字列が見つからなければ失敗
#          print('NO')
#          break
 
#      # 文字が含まれていた場合
#      if idx == len(kchars) - 1:
#          # 含まれていた文字列が、最後の文字'e'だった場合、成功
#          print('YES')
#          break
#      else:
#          char_index = remaining_string.index(char)
#          remaining_string = S[current_position + char_index + 1:]
#          current_position += char_index + 1
