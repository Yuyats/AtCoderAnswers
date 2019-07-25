import numpy as np


def main():
    N, K = map(int, input().split())
    C = []
    V = []
    for i in range(N):
        c, v = map(int, input().split())
        C.append(c)
        V.append(v)

    print(-1)
    for i in range(2, N):
        unq, unq_idx, unq_cnt = np.unique(C, return_inverse=True, return_counts=True)
        cnt_mask = unq_cnt > 1
        dup_ids = unq[cnt_mask]
        print(dup_ids)



main()
