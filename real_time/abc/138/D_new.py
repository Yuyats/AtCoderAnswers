import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def dfs(v: int, p: int) -> None:
    for u in T[v]:
        if u != p:  # p: parent -> skip
            cnt[u] += cnt[v]  # cumulative sum
            dfs(u, v)


def main():
    # Ai (A[i][0]) may be not a parent of Bi (A[i][1])
    global T, cnt
    N, Q = tuple(map(int, input().split()))  # vertices and queues
    E = tuple(tuple(map(int, input().split())) for _ in range(N - 1))
    P = tuple(tuple(map(int, input().split())) for _ in range(Q))
    T = [[] for _ in range(N + 1)]  # tree, (N+1: 1-idx -> 0-idx)
    for a, b in E:
        T[a] += [b]
        T[b] += [a]
    cnt = [0] * (N + 1)
    for p, x in P:
        cnt[p] += x  # increase vertex p by x
    dfs(1, -1)
    print(*cnt[1:])


if __name__ == "__main__":
    main()
