'''
문제 : 쉬운 최단거리 (14940)
난이도 : 실버1
'''
import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().strip().split()))
         for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

init = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            init = [i, j]
        if graph[i][j] == 0:
            visited[i][j] = 0

q = deque([init])
visited[init[0]][init[1]] = 0

while (q):
    c = q.popleft()
    x = c[0]
    y = c[1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx < 0 or nx >= n or ny < 0 or ny >= m):
            continue

        if visited[nx][ny] != -1:
            continue

        if graph[nx][ny] == 1:
            q.append([nx, ny])
            visited[nx][ny] = visited[x][y] + 1

for i in visited:
    for j in i:
        print(j, end=' ')
    print()
