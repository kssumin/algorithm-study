'''
문제 : 치즈
난이도 : 골드4

치즈가 모두 녹아서 없어지는 데 걸리는 시간 & 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 잇는 칸의 개수

cheeze 개수가 0이 될 때까지 (0, 0)에서 bfs 시작~~
1. 현재 cheeze 개수 count
2. (0, 0)에서 bfs 시작
'''
import sys
from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
cheeze = 0

# 입력
# height, width 입력
h, w = map(int, sys.stdin.readline().split())

# 그래프 입력
graph = []
for _ in range(h):
    graph.append(list(map(int, sys.stdin.readline().split())))

# function
# 현재 cheeze 개수 count


def cheezeCount():
    count = 0
    for g in graph:
        count += g.count(1)
    return count


# (0, 0)에서 bfs 시작
# 1 만나면 melt에 추가 -> 일괄적으로 0으로 만들기
q = deque()
melt = deque()


def bfs():
    q.clear()
    melt.clear()
    visited = [[False] * w for _ in range(h)]
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == False:
                visited[nx][ny] = True
                if graph[nx][ny] == 1:
                    melt.append((nx, ny))
                elif graph[nx][ny] == 0:
                    q.append((nx, ny))
    for x, y in melt:
        graph[x][y] = 0


count = 0
while True:
    curr = cheezeCount()
    if cheezeCount() > 0:
        count += 1
        cheeze = curr
        bfs()
    else:
        print(count)
        print(cheeze)
        break
