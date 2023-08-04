'''
/*문제 정보 */
7562번 - 나이트의 이동
난이도 - 실버 1
/*풀이 방법 */
bfs 로 그래프에서 이동시마다 1을 올리고 도착점에 도달하면 -1 해서 출력해주었다.
'''
from collections import deque
import sys
input = sys.stdin.readline

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [1,-1,2,-2,2,-2,1,-1]

def bfs(a,b):
    queue = deque()
    queue.append((a,b))

    while queue:
        i, j = queue.popleft()
        if i == x and j == y:
            return graph[i][j] - 1

        for k in range(8):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == 0:
                graph[nx][ny] = graph[i][j] + 1
                queue.append((nx,ny))

t = int(input())
for _ in range(t):
    l = int(input())
    a, b = map(int, input().split())
    x, y = map(int, input().split())
    graph = [[0] * l for _ in range(l)]
    graph[a][b] = 1
    print(bfs(a,b))

'''
/*오답 노트*/
/*느낀 점*/
나이트의 이동 dx, dy 가 다른 문제와 다른 것 말고는 다른 게 없어 나름 쉽게 풀
수 있었다.
'''