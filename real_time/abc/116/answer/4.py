n,k = map(int,input().split())
top = [0]*n
print('top', top)
sub = []
for i in range(n):
    t,d = map(int,input().split())
    t -=1
    if top[t]==0:
        top[t]=d
    else:
        if top[t]>=d:
            sub.append(d)
        else:
            sub.append(top[t])
            top[t]=d
print(top) 
top.sort()
print(top) 
top = top[::-1]
print(top) 
res = [0]
for i in range(n):
    if top[i]!=0:
        res.append(res[-1]+top[i])
    else:
        res.append(-1)
print('sub', sub)
sub.sort()
print('sub', sub)
sub = sub[::-1]
print('sub', sub)
w = [0]
for i in range(len(sub)):
    w.append(w[-1]+sub[i])
tmp = 0
for i in range(1,k+1):
    if len(w)-1>=k-i and res[i]!=-1:
        tmp = max(res[i]+w[k-i]+i*i,tmp)
 
print(tmp)
    
