import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools, os, pdb
sys.setrecursionlimit(10**7)
from queue import PriorityQueue
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
def perr(s): return print(s, file=sys.stderr)
N, M = LI()
data = []
c_list =[]
combi_dict = {}
for m in range(M):
    a,b = LI()
    c = LI()
    data.append([a, b, c])
    c_key = ','.join([str(i) for i in c])
    if combi_dict.get(c_key) is None:
        combi_dict[c_key] = a
    else:
        combi_dict[c_key] = min(combi_dict[c_key], a)
#  perr(data)
#  perr(combi_dict)

# すべて開けることができない場合を除外
done_list = []
for d in data:
    for c in set(d[2]):
        if c not in done_list:
            done_list.append(c)
#  print(done_list)
if len(done_list) != N:
    print(-1)
    exit()

# 全部の箱を開けるということで、まず1の箱、2の箱というようにやる？
"""
まずどの鍵を使えばいいか
DPは？
単純にやると、どの鍵を使うかの組み合わせ全部求める
それだと最大MC12通りになる
鍵は1000個しかないことに注目
そもそも12個しか箱がないので、例えば、同じ組み合わせの箱をあけるとすると、無駄な鍵が絶対ある
例えば
1000円で1,2,3を開ける鍵と、100円で1,2,3を開ける鍵がある場合
減らせる
後は、箱番号ごとにリストにして、ひとつになるまで減らす
高いやつは怪しい
まず仮ぎめして、これ以上安くできるか検証
[[],
[['1,3,4', 67786, 22595.333333333332]],
[['2', 3497, 3497.0], ['2,3,4', 2156, 718.6666666666666]],
[['1,3,4', 67786, 22595.333333333332], ['2,3,4', 2156, 718.6666666666666], ['3', 86918, 86918.0]],
[['1,3,4', 67786, 22595.333333333332], ['2,3,4', 2156, 718.6666666666666]]
]
これなら
1 3 4
2
にして、1 3 4でまず検討
まず平均最低から決定

---
 ----
--
  -----
   ----
"""

kv_list = [[] for _ in range(0, N+1)]
for key, value in combi_dict.items():
    key_list =list(map(int, key.split(',')))
    length = len(key_list)
    average = value/len(key_list)
    for k in key_list:
        kv_list[k].append([key, value, average, length])
#  print(kv_list)
ans = []
#  kv_list.sort(key=lambda x: x[2])

for idx, kv in enumerate(kv_list):
    if len(kv) == 0: continue
    min_v = min([i[1] for i in kv])
    for item_idx, item in enumerate(kv):
        if item[3] == 1 and item[1] != min_v:
            del kv_list[idx][item_idx]
            break
#  print(kv_list)
data = [j for i in kv_list for j in i]
#  print(data)
# ここから組み合わせを求める
ans = inf
def dfs(idx, price, opened_list):
    if idx == M:
        if len(opened_list) == N:
            #  print(idx, price, opened_list)
            global ans
            ans = min(ans, price)
        return

    # 単純に使う場合、使わない場合
    next_v = data[idx]
    if not all(x in opened_list for x in next_v):
        keys = list(map(int, next_v[0].split(',')))
        new_opened = list(set(opened_list + keys))
        dfs(idx + 1, price+next_v[1], new_opened)
        dfs(idx + 1, price, opened_list)
dfs(0, 0, [])
print(ans)
"""
i本目のときに、k個箱開けられてて、いくら
もし更新できるならする
とりあえず平均低いやつから選ぶか
逆に全部使って、どれなら取れるか？
"""
