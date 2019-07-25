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
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def pf(s): return print(s, flush=True)
"""
全通りは4**N通り存在する
その中から、ダメな通りを覗いたら答えになる
例えば、AGCを含む通りは、AGCを何番目に置くかとそのほかの数字を4*4*していく
"""
# 直前の4文字を見てdpする
"""
例えば1文字目で直前がaaa, aac, aag, aat, acc, ... 
と続いていくと、
"""
dp = []
N = I()
INF = 10**9 + 7
memo = [{} for i in range(N+1)]

def ok(last4):
    for i in range(4):
        t = list(last4)
        if i >= 1:
            t[i-1], t[i] = t[i], t[i-1]
        if ''.join(t).count('AGC') >= 1:
            return False

    return True

def dfs(cur, last3):
    import pdb
    pdb.set_trace()
    if last3 in memo[cur]:
        return memo[cur][last3]
    if cur == N:
        return 1
    ret = 0
    for c in "ACGT":
        if ok(last3 + c):
            ret = (ret + dfs(cur + 1, last3[1:] + c)) % INF
    memo[cur][last3] = ret
    return ret

print(dfs(0, "TTT"))

#  # N >= 4じゃないとだめ。
#  # どうやらAGCだと長さが倍、倍になっていくと惹かなければ行けないものも増えていく
#  all_patterns = 4**N

#  # AGCがどこにあるか、に、埋まってないところの穴埋めをする
#  AGC_patterns = (N-3+1)*(4**(N-3))
#  # 後ろにあと何回３のセットが作れるかで変わってくる
#  red = 0
#  for i in range(N-3):
#      tmp = N-3-i
#      red += tmp//3
#  AGC_patterns -= red

#  ACG_patterns = GAC_patterns = AGC_patterns
#  print('all', all_patterns)
#  print('agc, acg, gac', AGC_patterns, ACG_patterns, GAC_patterns)
#  result = all_patterns - AGC_patterns - ACG_patterns - GAC_patterns
#  print(result%INF)
