n, m = list(map(int, input().split()))
xxx = list(map(int, input().split()))
 
if n >= m:
    print(0)
    exit()
xxx.sort()
ddd = [b - a for a, b in zip(xxx, xxx[1:])]
ddd.sort()
print(sum(ddd[:m - n]))
