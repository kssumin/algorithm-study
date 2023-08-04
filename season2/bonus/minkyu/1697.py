import sys
from collections import deque
input = sys.stdin.readline


def bfs(start, count):
    queue = deque([[start, count]])
    visited[start] = True
    while queue:
        now, cnt = queue.popleft()
        if now == K:
            print(cnt)
            break
        if 0 <= now * 2 < 100001 and not visited[now * 2]:
            visited[now * 2] = True
            queue.append([now * 2, cnt + 1])
        if 0 <= now + 1 < 100001 and not visited[now + 1]:
            visited[now + 1] = True
            queue.append([now + 1, cnt + 1])
        if 0 <= now - 1 < 100001 and not visited[now - 1]:
            visited[now - 1] = True
            queue.append([now - 1, cnt + 1])
    return


N, K = map(int, input().split())
visited = [False for _ in range(100001)]
bfs(N, 0)

"""
풀이
BFS로 풀어야겠다고 생각했다!
미로 문제에서 하나씩 뻗어가는것처럼 이것도 하나씩 queue에 숫자와 함께 count를 추가한다.
count가 적은 순으로 queue에 쌓이므로 가장 빠른시간이 몇 초인지 구할 수 있다!
"""