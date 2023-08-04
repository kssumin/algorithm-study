import sys
from collections import deque
input = sys.stdin.readline


M, N = map(int, input().split())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(N):
    graph.append(list(map(int, input().split())))

queue = deque([])
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j, 0))
while queue:
    x, y, degree = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny, degree + 1))
can_go = True
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            can_go = False
if can_go:
    print(degree)
else:
    print(-1)

"""
일단 한 칸씩 진행해야해서 bfs를 썼다.
그랬더니 잘 풀렸다.
"""