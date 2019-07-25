import heapq
n,k=map(int,input().split())
data=[]
for i in range(n):
    t,d=map(int,input().split())
    data.append((-d,t))
data=sorted(data)
print(data)
neta=set()
que1=[]
p,x=0,0
for i in range(k):
    if data[i][1] in neta:
        heapq.heappush(que1,(-data[i][0],data[i][1]))
        x-=data[i][0]
    else:
        x-=data[i][0]
        p+=1
        neta.add(data[i][1])
print(heapq)
print(neta)
print(x)
mx=x+p*p
for i in range(k,n):
    if data[i][1] in neta:
        # すでに選択済みのものは放置
        pass
    else:
        # まだないネタであれば
        if que1:
            a=heapq.heappop(que1)
            x=x-a[0]-data[i][0]
            p+=1
            neta.add(data[i][1])
            mx=max(mx,x+p*p)
        else:
            break
print(mx)
