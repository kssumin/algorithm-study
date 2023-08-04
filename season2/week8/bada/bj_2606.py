'''
문제 : 바이러스(2606)
난이도 : 실버3

컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어짐
-> 노드 개수와 간선 정보 제공

1번 컴퓨터가 바이러스에 걸렸을 때 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수 출력

dfs나 bfs해서 개수 counting 하면 되겠다!
'''
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x):
    visited[x] = 1
    for nx in graph[x]:
        if visited[nx] == 0:
            dfs(nx)


dfs(1)
print(sum(visited) - 1)


'''
# bfs 방법
from collections import deque

visited[1] = 1
queue = deque([1])

while queue:
    c = queue.popleft()
    for nx in graph[c]:
        if visited[nx] == 0:
            queue.append(nx)
            visited[nx] = 1
'''
