import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
distance = [INF for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    node1, node2, dist = map(int, input().split())
    graph[node1].append((dist, node2))
    graph[node2].append((dist, node1))

queue = []
heapq.heappush(queue, (0, 1))
distance[1] = 0
visited[1] = True
while queue:
    dist, now = heapq.heappop(queue)
    if distance[now] < dist:
        continue
    for path in graph[now]:
        if not visited[path[1]] and path[0] + dist < distance[path[1]]:
            distance[path[1]] = path[0] + dist
            heapq.heappush(queue, (distance[path[1]], path[1]))
    visited[now] = True
print(distance[-1])

"""
풀이
그냥 다익스트라 알고리즘을 써서 풀었다.

오랜만에 다익스트라 문제를 풀었더니 기억이 안 나서 이론을 다시 봤다.
그런데도 헷갈려서 숫자 하나씩 틀려서 몇 번 틀렸다.

"""