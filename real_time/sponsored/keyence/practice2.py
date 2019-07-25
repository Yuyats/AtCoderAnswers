S = str(input())

kchars = ['k', 'e', 'y', 'e', 'n', 'c', 'e']

remaining_string = S
for idx, char in enumerate(kchars):
    if char not in remaining_string:
        # 文字列が見つからなければ失敗
        print('NO')
        break

    if idx == len(kchars) - 1:
        # 含まれていた文字列が、最後の文字'e'だった場合、成功
        print('YES')
        break
    else:
        char_index = S.index(char)
        remaining_string = S[char_index + 1:]
