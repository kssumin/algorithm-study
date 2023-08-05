import sys
input = sys.stdin.readline


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
dp1 = [[0 for _ in range(N)] for _ in range(N)]
dp2 = [[0 for _ in range(N)] for _ in range(N)]
dp3 = [[0 for _ in range(N)] for _ in range(N)]
dp1[0][1] = 1
for i in range(N):
    for j in range(2, N):
        if graph[i][j] != 1:
            if 0 <= j - 1 < N:
                # 가로 to 가로
                dp1[i][j] += dp1[i][j-1]
                # 대각 to 가로
                dp1[i][j] += dp3[i][j-1]
            if 0 <= i - 1 < N:
                # 세로 to 세로
                dp2[i][j] += dp2[i-1][j]
                # 대각 to 세로
                dp2[i][j] += dp3[i - 1][j]
            if 0 <= i - 1 < N and 0 <= j - 1 < N and graph[i-1][j] == 0 and graph[i][j-1] == 0:
                dp3[i][j] += dp1[i-1][j-1]
                dp3[i][j] += dp2[i-1][j-1]
                dp3[i][j] += dp3[i-1][j-1]
        elif graph[i][j] == 1:
            dp1[i][j], dp2[i][j], dp3[i][j] = 0, 0, 0
print(dp1[-1][-1] + dp2[-1][-1] + dp3[-1][-1])


"""
풀이
처음에 bfs로 풀었는데 시간 초과가 났다.
알고보니 bfs가 아니라 그냥 브루트 포스로 풀었다.
그냥 큐를 사용한 전체탐색이다.

도저히 안 풀려서 질문 게시판에서 힌트를 얻었다.
파이썬으로는 bfs나 dfs로는 풀기 힘들고 dp로 풀어야한다.
그래서 dp로 풀었다. 자세한 풀이는 발표 자료에...
i, j에 파이프의 마지막 부분이 닿았을 때 파이프의 형태는 가로, 세로, 대각선으로 세 가지이다.

1. 가로
가로로 누우려면
  1. 가로 to 가로
  2. 대각선 to 가로
2. 세로
세로로 누우려면
  1. 세로 to 세로
  2. 대각선 to 세로
3. 대각선
  1. 가로 to 대각선
  2. 세로 to 대각선
  3. 대각선 to 대각선

따라서 가로, 세로, 대각선의 dp[-1][-1]를 더하면 정답이 나온다.

bfs 풀이

import sys
from collections import deque
input = sys.stdin.readline

def can_go(dot1, dot2, op):
    x1, y1 = dot1
    x2, y2 = dot2
    if op == 1:
        if y2 + 1 < N and graph[x2][y2 + 1] == 0:
            queue.append(((x1, y1 + 1), (x2, y2 + 1), 1))
        if y2 + 1 < N and x2 + 1 < N:
            for x, y in ((x2, y2 + 1), (x2 + 1, y2), (x2 + 1, y2 + 1)):
                if graph[x][y] == 1:
                    break
            else:
                queue.append(((x2, y2), (x2 + 1, y2 + 1), 3))
    elif op == 2:
        if x2 + 1 < N and graph[x2 + 1][y2] == 0:
            queue.append(((x1 + 1, y1), (x2 + 1, y2), 2))
        if x2 + 1 < N and y2 + 1 < N:
            for x, y in ((x2, y2 + 1), (x2 + 1, y2), (x2 + 1, y2 + 1)):
                if graph[x][y] == 1:
                    break
            else:
                queue.append(((x2, y2), (x2 + 1, y2 + 1), 3))
    elif op == 3:
        if y2 + 1 < N and graph[x2][y2 + 1] == 0:
            queue.append(((x2, y2), (x2, y2 + 1), 1))
        if x2 + 1 < N and graph[x2 + 1][y2] == 0:
            queue.append(((x2, y2), (x2 + 1, y2), 2))
        if x2 + 1 < N and y2 + 1 < N:
            for x, y in ((x2, y2 + 1), (x2 + 1, y2), (x2 + 1, y2 + 1)):
                if graph[x][y] == 1:
                    break
            else:
                queue.append(((x2, y2), (x2 + 1, y2 + 1), 3))


N = int(input())
graph = []
cnt = 0
for _ in range(N):
    graph.append(list(map(int, input().split())))
queue = deque([((0, 0), (0, 1), 1)])
if graph[-1][-1] != 1:
    while queue:
        dot1, dot2, op = queue.popleft()
        if dot2[0] == N - 1 and dot2[1] == N - 1:
            cnt += 1
        can_go(dot1, dot2, op)
print(cnt)
"""