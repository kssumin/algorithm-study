from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    dx = [1, 0, 1]
    dy = [0, 1, 1]
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        for i in range(3):
            new_x, new_y = x + dx[i], y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < M:
                if candy[x][y] + maze[new_x][new_y] > candy[new_x][new_y]:
                    queue.append((new_x, new_y))
                    candy[new_x][new_y] = candy[x][y] + maze[new_x][new_y]
    return candy[N-1][M-1]


N, M = map(int, input().split())

maze = []
candy = [[-1 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    maze.append(list(map(int, input().split())))
candy[0][0] = maze[0][0]
print(bfs((0,0)))
"""
처음에 무슨 이상한 bfs와 brute force를 합친 이상한 코드를 작성했는데 메모리초과가 떴다.
메모리 초과는 고쳤는데 이제는 시간 초과가 떴다. bfs를 제대로 써야하는데 이상하게 써서 그런 것 같다.
처음에 candy 값을 전부 0으로 초기화했더니 사탕이 0인 길은 못 가게 되었다.
그래서 -1로 바꿔주었더니 잘 된다.
풀이
bfs로 풀었는데 게시판을 보니 dp가 더 좋아보인다. 미로 문제라고 dfs bfs만 생각하면 안되겠다.
"""