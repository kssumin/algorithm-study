import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    dp = [0 for _ in range(N+4)]
    dp[1], dp[2], dp[3], dp[4] = 1, 1, 1, 2
    for i in range(5, N + 1):
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[N])