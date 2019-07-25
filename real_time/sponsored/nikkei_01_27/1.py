def main():
    N, A, B = map(int, input().split())
    if N == A and N == B:
        # 全員が両方読んでいる場合
        print(N, N)
        return

    max_result = max([A, B])
    min_result = min([A, B])
    if A + B > N:
        # AとBの合計がNより大きい場合、最大は小さい方の数、最小はmin - (N - max)
        print(min_result, min_result - (N - max_result))
    elif A + B <= N:
        # AとBの合計がNより小さい場合、最大は小さい方の数、最小は0
        print(min_result, 0)



main()
