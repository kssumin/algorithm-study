import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def dfs(x, y):
    global cnt
    if not visited[x][y]:
        visited[x][y] = True
        if graph[x][y] == 1:
            cnt += 1
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if not visited[nx][ny]:
                        dfs(nx, ny)


N = int(input())
graph = []
result = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))
visited = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        dfs(i, j)
        if cnt != 0:
            result.append(cnt)
            cnt = 0
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])

"""
그냥 dfs인데 두 번 틀렸다.
습관처럼 쓰던 식을 써서 틀렸다. 없어도 되는 식인데...
모르는 것보다 대충 아는게 더 안 좋은 건데 dfs bfs를 이제 잘 한다고 생각했는데 더 해야겠다!

풀이
그냥 dfs를 썼다.
"""