import sys
sys.setrecursionlimit(100000)
#import numpy as np
input = sys.stdin.readline


def dfs(x, y):
    graph[x][y] = '|'
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0:
                graph[nx][ny] = '|'
                dfs(nx, ny)
def dfs2(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0:
                dfs(nx, ny)


N, M = map(int, input().split())
graph = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N):
    graph.append(list(map(int, input().split())))

dfs(0, 0)
hour = 0
count = 1
count_list = []
while count != 0:
#    print(np.array(graph))
#    print("------------------------------------------------------")
    count = 0
    hour += 1
    for x in range(N):
        for y in range(M):
            if graph[x][y] == '|':
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < N and 0 <= ny < M:
                        if graph[nx][ny] == 1:
                            graph[nx][ny] = '*'
                            count += 1
    for x in range(N):
        for y in range(M):
            if graph[x][y] == '*':
                graph[x][y] = '|'
    count_list.append(count)
    for x in range(N):
        for y in range(M):
            if graph[x][y] == '|':
                dfs2(x, y)


print(hour - 1)
if count_list[0] != 0:
    print(count_list[-2])
else:
    print(0)

"""
바깥 테두리를 찾는게 굉장히 어려웠다.
또 반례를 찾는데 시간이 굉장히 굉장히 굉장히 많이 걸렸다.
치즈 안에 치즈가 있고 그 사이에 공기가 들어있을 때 안쪽 치즈가 녹지 않아야한다.
치즈가 한 번이라도 녹기 전에는 안쪽 치즈를 녹지 않게 했었는데 한 번이라도 녹은 후 부터는 안쪽 치즈가 녹아버리게 코드를 짜 버렸다

오답 코드
for x in range(N):
        for y in range(M):
            if graph[x][y] == 0:
                dfs(x, y)
정답 코드
for x in range(N):
    for y in range(M):
        if graph[x][y] == '|':
            dfs2(x, y)
처음에는 잘 처리했지만 while문에 들어서면서부터 공기를 찾을 때 전체 탐색으로 찾아서 틀렸었다. 
"""