import numpy as np


def main():
    N = int(input())
    A = []
    B = []
    for i in range(0, N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    takahashi = 0
    aoki = 0
    # 足し算して一番大きいところからとる
    A = np.array(A)
    B = np.array(B)
    sum_AB = A + B
    l = sum_AB.argsort()[::-1]
    takahashi = sum([A[i] for i in [j for idx, j in enumerate(l) if idx % 2 == 0]])
    aoki = sum([B[i] for i in [j for idx, j in enumerate(l) if idx % 2 != 0]])

    print(int(takahashi - aoki))


main()
