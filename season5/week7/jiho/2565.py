import sys; input = sys.stdin.readline
lines = []
line = int(input())
dp = [1] * line
for i in range(line):
    start, end = map(int, input().split())
    lines.append([start, end])

lines.sort()
for i in range(line):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(line - max(dp))
