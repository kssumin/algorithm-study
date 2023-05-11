'''
/*문제 정보 */
2667번 - 단지번호붙이기
난이도 - 실버 1
/*풀이 방법 */
1인 곳에 위치하면 bfs 로 연결된 1을 계속찾아 0으로 바꿔주고 끝이나면
카운트를 저장해주는 것을 반복해주었다.
'''
import sys
from collections import deque

n = int(input())
graph = []
result = []

for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((x,y))

    graph[x][y] = 0
    count = 1
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1

    result.append(count)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i,j)

result.sort()
print(len(result))

for k in result:
    print(k)
'''
/*오답 노트*/
이상하게 출력이 되는 풀이..
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
result = []

def dfs(a,b,count):
    graph[b][a] = 0
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if (0 <= x < n) and (0 <= y < n) and graph[y][x]:
            count = dfs(x, y, count+1)
    return count


for j in range(n):
    for k in range(n):
        if graph[j][k]:
            result.append(dfs(j, k, count=1 ))

result.sort()

print(len(result))
for l in range(len(result)):
    print(result[l])
/*느낀 점*/
처음에 bfs 로 푼다고 적었던 것이 생각해보니 dfs 였다.. 다음 날에 다 지우고
처음부터 적었다. 근데 기본 틀은 bfs dfs 비슷한 것 같다.
'''