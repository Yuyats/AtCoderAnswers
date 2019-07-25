n,m=map(int,input().split())
X=sorted(list(map(int,input().split())))
ans=[]
if m<n:
  print(0)
  exit()
print('m-1', m-1)
for i in range(m-1):
  ans.append(X[i+1]-X[i])
print('ans', ans)
ans=sorted(ans)
print('ans{:m-n}', ans[:m-n])
print(sum(ans[:m-n]))
