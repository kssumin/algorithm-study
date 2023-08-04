import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
op1, op2 = map(int, input().split())
m = int(input())
family = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
for _ in range(m):
    parent, child = map(int, input().split())
    family[parent].append(child)
    family[child].append(parent)

queue = deque([(op1, 0)])
visited[op1] = True
while queue:
    relation, degree = queue.popleft()
    if relation == op2:
        print(degree)
        break

    if family[relation]:
        for person in family[relation]:
            if not visited[person]:
                queue.append((person, degree + 1))
                visited[person] = True
else:
    print(-1)

"""
방문처리를 하지 않고 직전 방문 노드를 체크하고 그 노드를 queue에 추가하지 않는 식을 짰는데 코드를 잘못 짜서 제대로 작동하지 않았다.
그래서 메모리 초과가 났다.
그냥 곱게 방문처리 식을 짜야겠다.
"""