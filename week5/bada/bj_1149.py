'''
문제 : RGB 거리
난이도 : 실버1
'''
import sys
input = sys.stdin.readline
n = int(input())

cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))

for i in range(1, n):
    cost[i][0] += min(cost[i-1][1], cost[i-1][2])
    cost[i][1] += min(cost[i-1][0], cost[i-1][2])
    cost[i][2] += min(cost[i-1][0], cost[i-1][1])

print(min(cost[-1]))
