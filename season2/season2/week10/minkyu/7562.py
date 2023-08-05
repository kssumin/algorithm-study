import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
list1 = [2, -2]
list2 = [1, -1]
for _ in range(N):
    I = int(input())
    x, y = map(int, input().split())
    tx, ty = map(int, input().split())
    visited = [[False for _ in range(I)] for _ in range(I)]
    visited[x][y] = True
    queue = deque([(x, y, 0)])
    while queue:
        x, y, degree = queue.popleft()
        if (x, y) == (tx, ty):
            print(degree)
            break
        for i in range(2):
            for j in range(2):
                nx, ny = x + list1[i], y + list2[j]
                nx2, ny2 = x + list2[i], y + list1[j]
                for x1, y1 in ((nx,ny), (nx2, ny2)):
                    if 0 <= x1 < I and 0 <= y1 < I:
                        if not visited[x1][y1]:
                            queue.append((x1, y1, degree + 1))
                            visited[x1][y1] = True

"""
뭔가 코드가 길어져서 슬프다.
이 문제도 하나씩 말을 옮기면서 찾아내는 문제라서 bfs를 써서 풀었다.
"""