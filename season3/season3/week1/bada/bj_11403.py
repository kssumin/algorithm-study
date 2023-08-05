'''
문제 : 경로 찾기
난이도 : 실버1

가중치가 없는 방향 그래프가 주어졌을 때 모든 정점에 대해서
i에서 j로 가는 경로가 *있는지 없는지* 구하는 프로그램


'''
import sys
from collections import deque

n = int(sys.stdin.readline())

# 그래프 인접 행렬 입력
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]


def bfs(x):
    queue = deque()
    queue.append(x)
    check = [0 for _ in range(n)]

    while queue:
        q = queue.popleft()

        for i in range(n):
            if check[i] == 0 and graph[q][i] == 1:
                queue.append(i)
                check[i] = 1
                visited[x][i] = 1


for i in range(0, n):
    bfs(i)

for i in visited:
    print(*i)
