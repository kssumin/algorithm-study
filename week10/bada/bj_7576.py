'''
문제 : 토마토
난이도 : 골드5

익은 토마토가 있는 칸의 상하좌우 칸에 담긴 토마토는 다음날 익는다
다 익을 때까지 걸리는 시간 구하기, 다 익지 못하는 경우는 -1

토마토가 있는 위치를 찾고, 방문 한 곳을 -1로 만들기(접근 금지!) 
더이상 움직일 곳이 없을 때 count가 n*m보다 작으면 -1
n*m과 같으면 answer 출력
'''
import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

m, n = map(int, sys.stdin.readline().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

count = 0
answer = 0
tomato = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            tomato.append((i, j))
            count += 1
        elif graph[i][j] == -1:
            count += 1

while (tomato):
    x, y = tomato.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 0:
            isValid = True
            tomato.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1
            count += 1

isValid = True
for t in graph:
    t = set(t)
    if (0 in t):
        isValid = False
        break
    else:
        answer = max(answer, max(t))

if (isValid):
    print(answer - 1)
else:
    print(-1)
