import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(x, y, count):
    global cnt
    if count > K:
        return False
    if x == 0 and y == C - 1:
        if count == K:
            return True
        return False
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and graph[nx][ny] != 'T':
            visited[nx][ny] = True
            if dfs(nx, ny, count + 1):
                cnt += 1
            visited[nx][ny] = False


R, C, K = map(int, input().split())
graph = []
visited = [[False for _ in range(C)] for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0
for _ in range(R):
    graph.append(list(input().rstrip()))

dfs(R-1, 0, 1)
print(cnt)

"""
풀이
dfs를 써서 백트래킹으로 풀었다
다만 다른 dfs문제와 다른 점은 21번째줄에 작성한거처럼 방문 처리했던 곳을 함수가 끝나고 나서는 False로 다시 바꾸어주는 것이다.
안 바꿔주면 길 하나만 찾게 되기 때문이다.
"""