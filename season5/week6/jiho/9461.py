#1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16
import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    a = int(input())
    dp = [0] * 101
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    for i in range(3, a+1):
        dp[i] = dp[i - 2] + dp[i - 3]
    print(dp[a])
