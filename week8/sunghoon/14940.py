'''
/*문제 정보 */
14940번 - 쉬운 최단거리
난이도 - 실버 1
/*풀이 방법 */
문제가 어려워 코드 리뷰 했습니다..!
https://emhaki.tistory.com/entry/python-%EB%B0%B1%EC%A4%80-14940%EB%B2%88-%EC%89%AC%EC%9A%B4-%EC%B5%9C%EB%8B%A8%EA%B1%B0%EB%A6%ACBFS
'''
import sys
input = sys.stdin.readline

from collections import deque
N, M = map(int, input().split())   # 주어진 n, m 값 받아주고
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]   # 방문하지 않은 곳은 -1
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]    # bfs 방향 설정


def bfs(i, j):
    queue = deque()
    queue.append((i, j))  # 시작 지점을 queue 에 넣어주기

    visited[i][j] = 0    # 방문 기록 해주고

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                if graph[nx][ny] == 0:    # 갈 수 없는 땅이면
                    visited[nx][ny] = 0   # 방문 처리만
                elif graph[nx][ny] == 1:    # 갈 수 있는 땅이면
                    visited[nx][ny] = visited[x][y] + 1   # 방문 처리에 +1
                    queue.append((nx, ny))    # 그리고 현재 좌표를 queue에 넣기


for i in range(N):
    for j in range(M):             # graph 의 값이 2 이고 방문을 하지 않은 곳에서
        if graph[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)             # bfs 실행

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:     # 그래프의 값이 0 일 때는 0을 출력
            print(0, end=' ')
        else:                   # 그래프이 값이 있다면 visited 값 출력
            print(visited[i][j], end=' ')
    print()
'''
/*오답 노트*/
/*느낀 점*/
처음 문제를 접할 때, dfs가 아닌 bfs로 풀어줘야 겠다고는 생각했다. 방문 기록을 저장하는 리스트를
만들어주고 반복문을 돌려 2인 지점에서 bfs 를 시작해야겠다는 것까지는 생각했으나, 거리 별로 값을
늘리는 방법에 대해 떠올리지 못해 풀지 못했다...
'''