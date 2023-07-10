N = int(input())
rgbs = []
for _ in range(N):
    rgbs.append(list(map(int, input().split())))

dp = [[0, 0, 0] for _ in range(N)]
dp[0] = rgbs[0]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgbs[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgbs[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgbs[i][2]

print(min(dp[N-1]))
