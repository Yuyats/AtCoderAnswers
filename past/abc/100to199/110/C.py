#  S = input()
#  T = input()

#  s_dict, t_dict = {}, {}

#  for i in range(len(S)):
#      if S[i] in s_dict.keys():
#          if s_dict[S[i]] != T[i]:
#              print("No")
#              exit()
#      else:
#          s_dict[S[i]] = T[i]

#      if T[i] in t_dict.keys():
#          if t_dict[T[i]] != S[i]:
#              print("No")
#              exit()
#      else:
#          t_dict[T[i]] = S[i]

#  print("Yes")




#  from collections import Counter
 
#  S = input()
#  T = input()
 
#  s = Counter(S)
#  t = Counter(T)
 
#  if sorted(s.values()) == sorted(t.values()):
#      print("Yes")
#  else:
#      print("No")



from collections import defaultdict

s = input()
t = input()

s_dict = defaultdict(int)
for char in s:
    s_dict[char] += 1

t_dict = defaultdict(int)
for char in t:
    t_dict[char] += 1

if sorted(s_dict.values()) == sorted(t_dict.values()):
    print("Yes")
else:
    print("No")





#  S = input()
#  T = input()
 
#  def to_num_list(s):
#      seen = {}
#      ret = []
#      idx = 0
#      for ch in s:
#          if ch not in seen:
#              seen[ch] = idx
#              idx += 1
#          ret.append(seen[ch])
#      return ret
 
#  if to_num_list(S) == to_num_list(T):
#      print('Yes')
#  else:
#      print('No')
