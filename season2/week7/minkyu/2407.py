import sys
input = sys.stdin.readline


n, m = map(int, input().split())
dp = [1 for _ in range(n + 1)]
for i in range(2, n + 1):
    dp[i] = dp[i-1] * i
print(dp[n] // (dp[n-m]*dp[m]))

"""
풀이
팩토리얼을 dp로 해서 풀었다.
"""