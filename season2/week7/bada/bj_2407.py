'''
문제 : 조합 (2407)
난이도 : 실버3

조합의 성질
nCr = n-1Cr + n-1Cr-1
'''
import sys

n, m = map(int, sys.stdin.readline().split())

dp = [[0] * (m+1) for _ in range(n+1)]
dp[1][0] = 1
dp[1][1] = 1

for i in range(2, n+1):
    for j in range(m+1):
        if j > i:
            break
        elif j == 0:
            dp[i][j] = 1
        elif j == 1:
            dp[i][j] = i
        elif j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

print(dp[n][m])
