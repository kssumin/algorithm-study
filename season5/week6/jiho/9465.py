import sys
input = sys.stdin.readline

T = int(input())
n = int(input())
sticker = [list(input().split()) for _ in range(2)]
visited = [[0] * n for _ in range(2)]

for i in range(T):
    visited[0][0] = sticker[0][0]
    visited[1][0] = sticker[1][0]
    if n == 1:
        maximum = max(visited[0][0], visited[1][0])
        print(maximum)
        continue

    visited[0][1] = sticker[1][0] + sticker[0][1]
    visited[1][1] = sticker[0][0] + sticker[1][1]
    if n == 2:
        maximum = max(visited[0][1], visited[1][1])
        print(maximum)
        continue

    for i in range(2, n):
        visited[0][i] = max(visited[1][i - 2], visited[1][i - 1]) + sticker[0][i]
        visited[1][i] = max(visited[0][i - 2], visited[0][i - 1]) + sticker[1][i]

    print(max(visited[0][-1], visited[1][-1]))





