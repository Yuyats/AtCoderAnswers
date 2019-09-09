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
def perr(s):
    if 'LOCAL' in os.environ:
        print(s)

def main():
    global PX, nodes
    if 'BIG' in os.environ:
        N = 2* 10** 5
        Q = 2 * 10 ** 5
        AB = [[i, i + 1] for i in range(1, N)]
        PX = [[i, 10] for i in range(Q)]
    else:
        N, Q = LI()
        #  AB = []
        nodes = [[] for _ in range(N+1)]
        PX = [0] * (N+1)
        for i in range(N-1):
            a, b = LI()
            #  AB += (a, b)
            nodes[a].append(b)
            nodes[b].append(a)

        for i in range(Q):
            p, x = LI()
            PX[p] += x
        dfs(1, -1)
        print(' '.join(map(lambda x: str(x), PX[1:])))
        #  for i in PX[1:]:
        #      print(i, end=' ')
        #  ans = [0 for _ in range(N)]

def dfs(parent, parent_parent):
    for node in nodes[parent]:
        if node != parent_parent:
            PX[node] += PX[parent]
            dfs(node, parent)

if __name__ == '__main__':
    main()

#      """
#      そもそも各頂点の部分木をdictに入れましょうか？
#      参照するような形で。
#      2には3
#      3には4,5
#      4,5はNoneだと、参照しやすいか？

#      カウントを若い順にやっていく
#      """
#      d = {}
#      for i in range(N+1):
#          d[i] = 0
#      for p, x in PX:
#          if p not in d.keys():
#              d[p] = 0
#          d[p] += x
#      perr(d)
#      """
#      根からスタートするとは？
#      1-5-3とかっていう組み合わせがあるため、dfsで根から辿っていく必要がある

#      """
#      global ans
#      ans = [0 for _ in range(N)]
#      ans[0] = d[1]

#      global lines_dict
#      lines_dict = {}
#      for ab in AB:
#          if ab[0] not in lines_dict.keys():
#              lines_dict[ab[0]] = {ab[1]}
#          else:
#              lines_dict[ab[0]].add(ab[1])

#          if ab[1] not in lines_dict.keys():
#              lines_dict[ab[1]] = {ab[0]}
#          else:
#              lines_dict[ab[1]].add(ab[0])

#      if 'LOCAL' in os.environ:
#          pdb.set_trace()
#      perr(lines_dict)
#      #  exit()




#          #  new_AB = []
#          #  target_lines = []
#          #  for ab in AB:
#          #      if current_node in ab and ab[0] not in done_list and ab[1] not in done_list:
#          #          target_lines.append(ab)
#          #      else:
#          #          new_AB.append(ab)
#          #  target_lines = [ab for ab in AB if current_node in ab and ab[0] not in done_list and ab[1] not in done_list]
#          #  if current_node not in lines_dict.keys():
#          #      return
#          #  target_lines = [num for num in lines_dict[current_node] if num not in done_list]
#          #  done_list.append(current_node)
#          #  for to_node in target_lines:
#          #      perr(to_node)
#          #      ans[to_node-1] = val + d[to_node]
#          #      dfs(to_node, ans[to_node-1], done_list)

#      dfs(1, d[1], None)
#      perr(ans)
#      print(' '.join(map(lambda x: str(x), ans)))


#  def dfs(current_node, val, parent_node):
#      for other_node in lines_dict[current_node]:
#          if other_node == parent_node:
#              continue
#          # まだ訪れていないので訪問
#          new_val = val + d[other_node]
#          ans[other_node-1] = new_val
#          dfs(other_node, new_val, current_node)

#  if __name__ == '__main__':
#      main()

#  #  for a, b in AB:
#  #      if b not in d.keys():
#  #          d[b] = 0
#  #      if a not in d.keys():
#  #          d[a] = 0
#  #      d[b] += d[a]
#  #  for i in range(1, N+1):
#  #      print(d[i], end=' ')









#  #  AB = sorted(AB, key=lambda x: x[1], reverse=True)

#  #  perr('AB')
#  #  perr(AB)
#  #  d = {}
#  #  pdb.set_trace()
#  #  for a, b in AB:
#  #      #  perr([a,b])
#  #      # abの頂点若い方に足していく
#  #      if a not in d.keys():
#  #          d[a] = []
#  #      if b not in d.keys():
#  #          d[a].append(b)
#  #      else:
#  #          d[a].append(b)
#  #          d[a].extend(d[b])

#  #  pdb.set_trace()
#  #  perr('d')
#  #  perr(d)

#  #  #  ans = [0 for _ in range(N)]
#  #  items_to_add = [0 for _ in range(N)]
#  #  for p, x in PX:
#  #      items_to_add[p-1] += x
#  #  perr(items_to_add)

#  #  ans = {}
#  #  for idx, item in enumerate(items_to_add):
#  #      if idx+1 not in ans.keys():
#  #          ans[idx+1] = 0

#  #      ans[idx+1] += item
#  #      if idx+1 not in d.keys():
#  #          continue
#  #      for i in d[idx+1]:
#  #          if i not in ans.keys():
#  #              ans[i] = 0
#  #          perr('i')
#  #          perr(i)
#  #          ans[i] += item

#  #  #  for p, x in PX:
#  #  #      perr('px')
#  #  #      perr([p, x])
#  #  #      ans[p-1] += x
#  #  #      if p not in d.keys():
#  #  #          continue
#  #  #      for i in d[p]:
#  #  #          perr('i')
#  #  #          perr(i)
#  #  #          ans[i-1] += x

#  #  perr('ans')
#  #  perr(ans)
#  #  for i in range(1, N+1):
#  #      print(ans[i], end=' ')
