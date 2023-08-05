import sys
input = sys.stdin.readline


def game():
    for i in range(N):
        for j in range(N):
            dfs(i, j, "row", 1)
            dfs(i, j, "column", 1)


def dfs(x, y, op, cnt):
    if 0 > x or x >= N or 0 > y or y >= N:
        return
    if op == "row":
        if not visited_row[x][y]:
            visited_row[x][y] = True
            if y + 1 < N and graph[x][y + 1] == graph[x][y]:
                dfs(x, y + 1, "row", cnt + 1)
            else:
                result.append(cnt)
    elif op == "column":
        if not visited_column[x][y]:
            visited_column[x][y] = True
            if x + 1 < N and graph[x + 1][y] == graph[x][y]:
                dfs(x + 1, y, "column", cnt + 1)
            else:
                result.append(cnt)


def switch(x1, y1, x2, y2):
    graph[x1][y1], graph[x2][y2] = graph[x2][y2], graph[x1][y1]
    return


N = int(input())
graph = []
result = []
for _ in range(N):
    graph.append(list(input().rstrip()))
for i in range(N):
    for j in range(N - 1):
        # row
        visited_row = [[False for _ in range(N)] for _ in range(N)]
        visited_column = [[False for _ in range(N)] for _ in range(N)]
        switch(i, j, i, j + 1)
        for k in range(j, j + 2):
            for l in range(i + 1):
                dfs(l, k, 'column', 1)
        for k in range(j + 1):
            dfs(i, k, 'row', 1)
        switch(i, j, i, j + 1)

        # column
        switch(j, i, j + 1, i)
        visited_row = [[False for _ in range(N)] for _ in range(N)]
        visited_column = [[False for _ in range(N)] for _ in range(N)]
        for k in range(j, j + 2):
            for l in range(i + 1):
                dfs(k, l, 'row', 1)
        for k in range(j + 1):
            dfs(k, i, 'column', 1)
        i, j = i, j
        switch(j, i, j + 1, i)

print(max(result))
"""
처음에는 가로로만 서로 바꿔주고 탐색해서 틀렸었다.
세로로도 바꾸는 식을 추가하고 제출했는데 시간초과가 났다.
알고보니 전체 탐색을 할 필요가 없었다. 
a와 b를 가로로 바꿔주었다면 a열과 b열 0 ~ 해당 행까지, 그리고 a와 b의 행을 0 ~ 해당 열까지 탐색해주면 되고,
a와 b를 세로로 바꿔주었다면 a행과 b행 0 ~ 해당 열까지, 그리고 a와 b의 열을 0 ~ 해당 행까지 탐색해주면 된다.
"""