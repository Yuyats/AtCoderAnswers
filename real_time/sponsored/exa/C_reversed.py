N, Q = map(int, input().split(' '))
S = '0' + input() + '0'
A = [list(input().split(' ')) for _ in range(Q)]
l = 0
r = N+1
for i in range(Q-1, -1, -1):
  t, d = A[i]
  if t == S[l] and d == 'R':
    l -= 1
  elif t == S[l+1] and d == 'L':
    l += 1
    
  if t == S[r] and d == 'L':
    r += 1
  elif t == S[r-1] and d == 'R':
    r -= 1
print(max(0, r-l-1))
