import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools

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

H, W = LI()
S = [input() for i in range(H)]


"""
マスの上下左右を確認する。
1辺のみの共有＝2頂点
隣り合う2辺の共有＝1頂点
3辺の共有=0
4辺の共有＝0
0辺の共有＝4

5 6
......
...#..
..###.
.##.#.
......

"""

ans = 0
for x in range(1, W-1):
    for y in range(1, H-1):
        # マスx，yの上下左右の色を確認
        up = S[y-1][x]
        down = S[y+1][x]
        right = S[y][x+1]
        left = S[y][x-1]

        #  print('--------')
        #  print(' ', up)
        #  print(left, ' ', right)
        #  print(' ', down)
        L = [up, down, right, left]

        black_count = L.count('#')

        if S[y][x] == '.':
            # 凹みを判定
            if black_count == 0:
                pass
            elif black_count == 1:
                pass
            elif black_count == 2:
                if up != down and right != left:
                    ans += 1
            elif black_count == 3:
                ans += 2
        else:
            if black_count == 0:
                print(4)
                exit()
            elif black_count == 3:
                pass
            elif black_count == 1:
                ans += 2
            elif black_count == 2:
                # 隣り合うか確認
                if up != down and right != left:
                    ans += 1
print(ans)
