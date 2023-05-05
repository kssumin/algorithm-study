import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
L = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
cnt = 0
for i in range(L):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

if len(visited) > 1:
    queue = deque([1])
    visited[1] = True
    while queue:
        node = queue.popleft()
        for connect_node in graph[node]:
            if not visited[connect_node]:
                visited[connect_node] = True
                queue.append(connect_node)
                cnt += 1
print(cnt)

"""
그냥 딱 bfs로 풀었다.
처음에 양방향 노드로 하지 않아서 틀렸었다.
"""