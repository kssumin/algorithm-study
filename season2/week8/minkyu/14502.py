import sys
from itertools import combinations
input = sys.stdin.readline


def dfs(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph_copy[nx][ny] == 0:
                graph_copy[nx][ny] = 2
                dfs(nx, ny)


N, M = map(int, input().split())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(N):
    graph.append(list(map(int, input().split())))

go_list = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            go_list.append((i, j))
safety_space = []
for wall1, wall2, wall3 in combinations(go_list, 3):
    x1, y1 = wall1
    x2, y2 = wall2
    x3, y3 = wall3
    graph_copy = [item[:] for item in graph]

    if wall1 == (0, 1) and wall2 ==(1,0) and wall3 == (3,4):
        pass
    graph_copy[x1][y1], graph_copy[x2][y2], graph_copy[x3][y3] = 1, 1, 1
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                dfs(i, j)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph_copy[i][j] == 0:
                cnt += 1
    safety_space.append(cnt)
print(max(safety_space))

"""
풀이
오잉 이게 되네?
벽을 어떤 조건으로 쳐야될지 모르겠어서 그냥 벽 세 개 치는 경우의 수를 다 돌린 후 그 중 최댓값을 출력하는 코드를 짰는데 됐다
"""