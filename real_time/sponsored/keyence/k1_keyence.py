n1, n2, n3, n4 = map(int, input().split())
if all([i in [n1,n2,n3,n4] for i in [1, 7, 9, 4]]):
    print('YES')
else:
    print('NO')
