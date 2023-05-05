import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
parent_node = [0 for _ in range(N + 1)]
for i in range(N - 1):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

queue = deque([1])
visited[1] = True
while queue:
    node = queue.popleft()
    for connect_node in graph[node]:
        if not visited[connect_node]:
            visited[connect_node] = True
            queue.append(connect_node)
            parent_node[connect_node] = node

for i in range(2, N + 1):
    print(parent_node[i])


"""
이 문제도 직전 2606문제와 같이 딱 bfs에다가
22번째줄만 추가해주었다.
1번이 루트이므로 1번부터 방문처리해주고 차례로 그래프를 탐색한다.
graph[x]에 있는 노드들 중 방문처리 되지 않은 노드의 부모 노드는 x이다.
그 중 방문 처리돼 있는 노드들은 이미 부모 노드를 찾은 노드들이다. 
"""