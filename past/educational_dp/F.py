import numpy as np

#  n = int(input())
#  m = int(input())

s = input()
t = input()

n = len(s)
m = len(t)

dp = [[0 for j in range(0,m)] for i in range(0, n)]
dp = np.array(dp)
print(dp)

for i in range(0, n):
    for j in range(0, m):
        print(i, j)
        print('====', i, j)
        if s[i] == t[j]:
            print('same', i, j)
            if i == 0:
                dp[i][j] = 1
            else:
                if len(set(dp[:i, j])) == 1:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + 1

            for k in range(j, m):
                dp[i][k] = dp[i][j]
            #  for l in range(i, n):
            #      dp[l][j] = dp[i][j]
        else:
            # はしっこにいる場合を考慮
            if j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i][:j])

for i in range(n):
    for j in range(m):
        if dp[i][j] == 0:
            if s[i] == t[j]:
                if i == 0:
                    dp[i][j] == 1
                else:
                    dp[i][j] = dp[i-1][j] + 1

                for k in range(j, m):
                    if s[i] != t[k]:
                        dp[i][k] = dp[i][j]
            else:
                if j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i][:j])

print([i for i in t])
for idx, i in enumerate(dp):
    print(s[idx], i)
