'''
문제 : 택배 배송
난이도 : 골드5

최소 신장 트리랑 최단 경로 알고리즘을 구분을 못 하고 있었다..!
이 문제는 최단 경로 찾기 문제!

다익스트라 혹은 플로이드 사용
'''
import sys
import math
import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dis[now] < d:
            continue
        for v, w in graph[now]:
            cost = d + w
            if cost < dis[v]:
                dis[v] = cost
                heapq.heappush(q, (cost, v))


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
dis = [math.inf]*(N+1)
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
dijkstra(1)
print(dis[N])
