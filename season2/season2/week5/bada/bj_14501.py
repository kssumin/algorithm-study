'''
문제: 퇴사
난이도: 실버3

#1
이런 문제 굉장히 많이 풀어봤는데..
'''
import sys
input = sys.stdin.readline

n = input()

dp = [0] * n
for i in range(n):
    t, p = map(int, input().split)
    if i + t < n:
        dp[i+t] = max(dp[i+t], dp[i+t-1])
