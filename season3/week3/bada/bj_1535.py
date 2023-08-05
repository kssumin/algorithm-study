'''
문제 : 안녕
난이도 : 실버2

이게 배낭문제인데, 중요한 건 배낭 문제를 어떻게 푸는지 까먹었다

이게 쪼갤 수 없으면 DP였고 쪼갤 수 있으면 그리디였던 건 기억나는데에,,,,

이중 for문 가보자
'''
import sys

n = int(sys.stdin.readline())

loss = [0] + list(map(int, sys.stdin.readline().split()))
happy = [0] + list(map(int, sys.stdin.readline().split()))

dp = [[0] * 101 for _ in range(n+1)]


for i in range(1, n+1):
    for j in range(1, 101):

        if j < loss[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-loss[i]] + happy[i])

print(dp[n][99])
