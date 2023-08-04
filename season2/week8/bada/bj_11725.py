'''
문제 : 트리의 부모 찾기(11725)
난이도 : 실버2

루트 없는 트리가 주어지면 각 노드의 부모를 구하는 프로그램?

'''
import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]  # 그래프 초기화
visited = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = 1
q = deque([1])
parents = [0] * (n+1)

while (q):
    c = q.popleft()
    for nx in graph[c]:
        if visited[nx] == 0:
            q.append(nx)
            parents[nx] = c
            visited[nx] = 1

for i in range(2, n+1):
    print(parents[i])
