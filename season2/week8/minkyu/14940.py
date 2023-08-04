import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
#n 세로
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(len(row)):
        if row[j] == 2:
            start = (i, j)
            graph[i][j] = 1
graph[start[0]][start[1]] = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque([start])
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] += graph[x][y]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = -1

for i in range(4):
    nx, ny = start[0] + dx[i], start[1] + dy[i]
    if 0 <= nx < n and 0 <= ny < m:
        if graph[nx][ny] != -1 and graph[nx][ny] != 0:
            graph[nx][ny] = 1

graph[start[0]][start[1]] = 0
for i in range(n):
    for j in range(m):
        print(graph[i][j], end=" ")
    print()

"""
풀이
처음에 graph를 만들 때 시작 위치를 저장하고 그 위치에서 bfs를 한다.
일단 시작 지점의 상하좌우 길 중에서 갈 수 있는 길을 1로 바꾸어준다.
그 길들은 갔던 길임에도 큐에 한 번 더 append하므로 일단 graph를 다 돈 후에 1로 바꾸어준다.
또, 길을 다 정한 다음에도 1인 곳이 있다면 길이 막혀있다는 뜻이니 1을 -1로 바꾼다.
"""