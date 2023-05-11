'''
문제 : 연구소
난이도 : 골드4


'''
import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().strip().split()))
         for _ in range(n)]

visited = [[0] * m for _ in range(n)]


init = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            init.append([i, j])
            visited[i][j] = 1
        if graph[i][j] == 1:
            visited[i][j] = 0

queue = deque(init)

while (queue):
    c = queue.popleft()
    x = c[0]
    y = c[1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (nx < 0 or nx >= n or ny < 0 or ny >= m):
            continue

        if visited[nx][ny] != 0:
            continue

        if graph[nx][ny] == 0:
            queue.append([nx, ny])
            visited[nx][ny] = 1

for i in range(n):
    for j in range(m):
        print(visited[i][j], end=" ")
    print()

count = 0
for i in visited:
    for j in i:
        if j == 0:
            count += 1
print(count)
