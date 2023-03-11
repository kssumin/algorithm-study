# BJ 1918 : 뱀 / GOLD IV / 68ms

import sys
from collections import deque

# n : 보드 한 변의 길이
n = int(sys.stdin.readline().strip())

# graph : n x n 게임보드
graph = [[0] * n for _ in range(n)]

# 순서대로 아래쪽, 오른쪽, 왼쪽, 위쪽으로 이동시켜주는 좌표
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# k개의 사과
k = int(sys.stdin.readline().strip())

for i in range(k):
    a, b = map(int, sys.stdin.readline().strip().split(' '))
    # print(a, b)
    graph[a - 1][b - 1] = 2


l = int(sys.stdin.readline().strip())
dirDict = dict()
queue = deque()
queue.append((0, 0))

for i in range(l):
    x, c = sys.stdin.readline().strip().split(' ')
    dirDict[int(x)] = c


x, y = 0, 0
graph[x][y] = 1
cnt = 0
direction = 0


def turn(alpha):
    global direction
    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4


while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]
    
    if x < 0 or x >= n or y < 0 or y >= n:
        break
    
    if graph[x][y] == 2:
        graph[x][y] = 1
        queue.append((x, y))
        if cnt in dirDict:
            turn(dirDict[cnt])
    
    elif graph[x][y] == 0:
        graph[x][y] = 1
        queue.append((x, y))
        tx, ty = queue.popleft()
        graph[tx][ty] = 0
        if cnt in dirDict:
            turn(dirDict[cnt])
    else:
        break
    
print(cnt)