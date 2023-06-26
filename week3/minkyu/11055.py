import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
dp = [0 for _ in range(N)]
dp[0] = num_list[0]
for i in range(1, N):
    for j in range(i-1, -1, -1):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j] + num_list[i])
    if dp[i] == 0:
        dp[i] = num_list[i]

print(max(dp))

"""
풀이
dp로 풀었다
dp는 언제나 어렵다 ㅠㅠㅠㅠ
"""
