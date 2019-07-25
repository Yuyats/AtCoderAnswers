import numpy as np
N = int(input())
A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))
 
if sum(A) < sum(B):
    re = -1
 
else:
    diff = A - B
    diff.sort()
 
    i = 0
    j = -1
    a = diff[j]
    while diff[i] < 0:
        a += diff[i] 
        while a<0:
            j -= 1
            a+= diff[j]
        i += 1
 
    if i == 0:
        re = 0
    else:
        re = i - j
 
print(re)
