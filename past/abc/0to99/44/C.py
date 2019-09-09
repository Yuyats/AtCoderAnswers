import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools,pdb
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

N, A = LI()
X = LI()

"""
1枚以上選んで平均をAにする
カードは50枚ある
選ぶか選ばないかで2**50通りある
2**10が1024だとすると
10**3を5回なので間に合わない

ソートして両端を求めるか
そもそも、50枚選んでAになるということ
50までなので、
A4なら
1 7
2 6
3 5
4 4
がある

7 9 8 9
の例で考えると
7 9が2通り
8が1通りある
7 9 7 9 7 9 7 9 7 9 だった場合

"""
ans = 0
def main():
    global ans
    def dfs(card_num, selected_cards):
        global ans
        if card_num == N:
            if selected_cards == []:
                return
            average = sum(selected_cards) / len(selected_cards)
            #  print(average, selected_cards)
            if average == A:
                #  print('equal')
                ans += 1
            return
        dfs(card_num+1, selected_cards + [X[card_num]])
        dfs(card_num+1, selected_cards)
    dfs(0, [])
if __name__ == "__main__":
    main()
    print(ans)
