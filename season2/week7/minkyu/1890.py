import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
def dfs(x, y):
    global cnt
    dx, dy = x + graph[x][y], y + graph[x][y]
    if (dx == N-1 and y == N-1) or (x == N-1 and dy == N-1):
        count[x][y] += 1
        cnt += 1
        return
    elif x == dx and y == dy:
        return
    for new_x, new_y in ((dx, y), (x, dy)):
        if 0 <= new_x < N and 0 <= new_y < N:
            if count[new_x][new_y] != 0:
                count[x][y] += count[new_x][new_y]
                cnt += count[new_x][new_y]
            else:
                dfs(new_x, new_y)
                if count[new_x][new_y] != 0:
                    count[x][y] += count[new_x][new_y]
N = int(input())
graph = []
count = [[0 for _ in range(N)] for _ in range(N)]
cnt = 0
for _ in range(N):
    graph.append(list(map(int, input().split())))
dfs(0,0)

print(cnt)

"""
정말 다양하게 틀렸다.
처음에는 그냥 썡 dfs만 썼더니 시간 초과, 두 번째는 그냥 틀림, 세 번째는 메모리 초과...

내가 쓴 방법은 일단 dfs를 쓰는데 (a, b)에서 (c, d)로 갔을 때 (c, d)가 가장 오른쪽 아래칸이라면 +1,
(c, d)가 0이라면 우측과 아래로 이동하고, 0이 아니면 (a, b) += (c, d)를 하고 더 이상 살펴보지 않는 것이다.

첫 번째와 세 번째 코드는 같은 이유로 틀린 것 같다.
graph가 0일 때를 고려하지 않아서 무한재귀를 돌아서 메모리 초과 또는 시간초과가 났다.

두 번째 코드가 틀린 이유는 20~21번째줄을 추가하지 않아서 틀렸다.

결과적으로 dfs + dp를 사용했다.

힘들게 풀어서 다른 사람의 코드를 살펴봤는데 다른 사람들은 그냥 간단하게 풀었다.
dp문제는 어려운 것 같다. 많이 풀어봐야겠다.
"""