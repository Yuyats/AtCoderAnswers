def main():
    N = int(input())
    A = str(input())
    B = str(input())
    C = str(input())

    count = 0
    for a, b, c in zip(A, B, C):
        unique_chars_length = len(set([a, b, c]))
        if unique_chars_length == 1:
            # すべて同じ文字のため操作は不要
            pass
        elif unique_chars_length == 2:
            # 文字が２種類存在するため、１回操作が必要
            count += 1
        elif unique_chars_length == 3:
            # 文字が３種類存在するため、２回操作が必要
            count += 2

    print(count)


main()
