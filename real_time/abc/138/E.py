import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools, os, pdb
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
def perr(s): return print(s, file=sys.stderr)

S = input()
T = input()

if any(i not in sorted(list(set(S))) for i in sorted(list(set(T)))):
    print(-1)
    exit()

d = {}
for sidx, s in enumerate(S):
    if s not in d.keys():
        d[s] = []
    d[s].append(sidx)

if 'LOCAL' in os.environ:
    print('d', d)
current = None
count = 0
ans = 0
for tidx, t in enumerate(T):
    #  pdb.set_trace()
    if 'LOCAL' in os.environ:
        print('--- t: ', t, tidx)
    if current == None:
        current = d[t][0]
        if 'LOCAL' in os.environ:
            print('current', current)
    else:
        # 1文字ごと見ていく
        b = bisect.bisect_left(d[t], current)
        if d[t][b] == current:
            # 前のindexと新しいindexが同じ場合うまくいかない
            if tidx == len(T) - 1:
                if b == len(d[t])-1:
                    # 最後のアイテム
                    count += 1
                    ans = 0
                    break
                else:
                    # 最後ではない
                    ans = d[t][b+1] + 1
                    break
            else:
                if b == len(d[t])-1:
                    count += 1
                    continue
                else:
                    b += 1

            # bが最後のアイテムでない限り
            b += 1

        if 'LOCAL' in os.environ:
            print('b', b)
            print('current', current)

        if b >= len(d[t]):
            count += 1
            # 超えている場合
            current = d[t][0]
            if tidx == len(T) - 1:
                # 最後の文字なので終わり
                ans = current+1
                # print('last1', ans)
                break
            else:
                # 続く
                # print('continue')
                continue
        else:
            # 文字列の最後の前に探している文字があった場合
            if tidx == len(T) - 1:
                # 最後の文字なので終わり
                # print('last2', d[t][b])
                ans = d[t][b]+1
                break
            else:
                # print('continue1')
                current = d[t][b]
                continue

        #  idx = d[t][b]
        #  print('=== idx', idx)
        #  if current <= idx:
        #      # もう一周
        #      current = d[t][0]
        #      if tidx == len(T) - 1:
        #          # 終わり
        #          ans += current+1
        #          break
        #      count += 1
#  perr('***count')
#  perr(count)
# print('ans ', ans)
print(len(S)*count + ans)




