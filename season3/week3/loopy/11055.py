# 115055 가장 큰 증가하는 부분 수열
# https://www.acmicpc.net/problem/11055
N = int(input())
arr = list(map(int, input().split()))

dp = [0] * N
dp[0] = arr[0]

for i in range(1, N):
    dp[i] = arr[i]
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))