# 길이가 1인 계단 수 : 1, 2, 3, 4, 5, 6, 7, 8, 9
# 길이가 2인 계단 수 : 12, 23, 34, 45, 56, 67, 78, 89, 10, 21, 32, 43, 54, 65, 76, 87, 98
# 1->2, 2->3, 3->4 ..... 8->9
# dp[자릿수][앞에 오는 숫자]
import sys
input = sys.stdin.readline

n = int(input())
dp = [[0] * 10 for _ in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)


