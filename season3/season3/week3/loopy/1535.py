# 1535 안녕
# https://www.acmicpc.net/problem/1535
N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

dp = [[0] * 101 for _ in range(N + 1)]

for i in range(0, N):
    for j in range(1, 101):
        if j < L[i]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - L[i]] + J[i])

print(dp[N][99])
