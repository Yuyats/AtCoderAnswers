import sys, itertools
def input(): return sys.stdin.readline()
def inpl(): return [int(i) for i in input().split()]
N, K = inpl()
Sushi = []
Neta = set()
ans = 0
for _ in range(N):
    t, d = inpl()
    Sushi.append((d, t))
Sushi.sort(reverse=True)
print('sushi', Sushi)
Db = []
Nd = []
for i in range(K):
    print('---- for i = ', i)
    d, t = Sushi[i]
    print('d, t, Neta, Db: ', d, t, Neta, Db)
    if t not in Neta:
        Neta.add(t)
        ans += d
    else:
        Db.append(d)
neta = len(Neta)
print('number of neta: ', neta)
print('Db before accumlate: ', Db)
print('ans: ', ans)
Db = [0] + list(itertools.accumulate(Db))
Db.reverse()
print('db', Db)
for i in range(N-K):
    print('---- for i = ', i)
    d, t = Sushi[K+i]
    print('d, t: ',d, t)
    if t not in Neta:
        Neta.add(t)
        Nd.append(d)
print('Neta, nd: ', Neta, Nd)
Nd = [0] + list(itertools.accumulate(Nd))
print(Nd)
print(ans + max([(neta + i)**2 + j + k for i, (j, k) in enumerate(zip(Db, Nd))]))
