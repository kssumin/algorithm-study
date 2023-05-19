'''
문제 : 네트워크 연결
난이도 : 골드4

최소신장트리(MST)
'''
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

edges = []
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))
edges.sort()


def findParent(parent, x):
    if parent[x] == x:
        return x
    else:
        return findParent(parent, parent[x])


def union(parent, a, b):
    rootA = findParent(parent, a)
    rootB = findParent(parent, b)
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB


result = 0
for edge in edges:
    cost, a, b = edge
    if findParent(parent, a) != findParent(parent, b):
        union(parent, a, b)
        result += cost

print(result)
