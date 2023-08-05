'''
문제 : 평범한 배낭
난이도 : 골드5
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

item = [[0, 0]]
for _ in range(n):
    item.append(list(map(int, input().split())))

DP = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        weight = item[i][0]
        value = item[i][1]
        if weight <= j:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-weight] + value)
        else:
            DP[i][j] = DP[i-1][j]
print(DP[n][k])
