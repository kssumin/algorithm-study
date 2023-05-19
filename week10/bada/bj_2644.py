'''
문제 : 촌수계산
난이도 : 실버2

여러 사람들에 대한 부모 자식들 간의 관계가 주어지면, 주어진 두 사람의 촌수를 계산해서 출력
'''
import sys
from collections import deque

n = int(sys.stdin.readline())
targetA, targetB = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

lines = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    lines[x].append(y)
    lines[y].append(x)

visited = [0] * (n+1)


def bfs(node):
    q = deque()
    q.append(node)
    while q:
        node = q.popleft()
        for n in lines[node]:
            if visited[n] == 0:
                visited[n] = visited[node] + 1
                q.append(n)


bfs(targetA)
if visited[targetB] > 0:
    print(visited[targetB])
else:
    print(-1)
