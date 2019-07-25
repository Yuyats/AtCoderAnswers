import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
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

N, M = LI()
lines = []
for m in range(M):
    lines.append(LI())

if M%2 == 1:
    # 辺の数がそもそも奇数なら無理
    print(-1)
    exit()
#  print(lines)
# 辺の数が偶数の場合
# 各頂点の辺の数を調べる。
# 奇数個の頂点は絶対に受ける側になる。
# 逆に偶数個の頂点はまずは2，4，6，。。。というふうに少ないところから確定していく
node_line_counts = [0 for i in range(N)]
for line in lines:
    node_line_counts[line[0]-1] += 1
    node_line_counts[line[1]-1] += 1
ans = []
while not all(i == 0 for i in node_line_counts):
    #  print('\nwhile')
    for cidx, c in enumerate(node_line_counts):
        # countが偶数のやつを抜き出す
        if node_line_counts[cidx] != 0 and node_line_counts[cidx] % 2 == 0:
            #  print('cidx, c', cidx, c)
            # 全部の辺を自分発信にする
            node_lines = [l for l in lines if cidx+1 in l]
            #  print('nls', node_lines)
            for nl in node_lines:
                node_line_counts[nl[0] - 1] -= 1
                node_line_counts[nl[1] - 1] -= 1
                lines.remove(nl)
                if nl[1] == cidx+1:
                    nl = [nl[1], nl[0]]
                ans.append(nl)
            # 数字を調整したらやり直す
#  print(ans)
for a in ans:
    print(a[0], a[1])
# 一周分の辺は出しておく

