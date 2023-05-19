'''
문제 : 나이트의 이동
난이도 : 실버1

나이트(출발 지점 -> 목표 지점) 최소 이동 횟수
'''
import sys
from collections import deque

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

t = int(sys.stdin.readline())

for _ in range(t):
    l = int(sys.stdin.readline())

    visited = [[0] * l for _ in range(l)]
    stx, sty = map(int, sys.stdin.readline().split())
    dex, dey = map(int, sys.stdin.readline().split())

    q = deque()
    q.append((stx, sty))

    while q:
        x, y = q.popleft()

        if x == dex and y == dey:
            print(visited[x][y])
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < l) and (0 <= ny < l) and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
