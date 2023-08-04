import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    count = 0
    visited[start] = True
    queue = deque([(start, count)])
    while queue:
        num, count = queue.popleft()
        if num == G:
            print(count)
            return
        if num + U <= F:
            if not visited[num + U]:
                queue.append((num + U, count + 1))
                visited[num + U] = True
        if num - D >= 1:
            if not visited[num - D]:
                queue.append((num - D, count + 1))
                visited[num - D] = True
    else:
        print("use the stairs")
        return


F, S, G, U, D = map(int, input().split())
visited = [False for _ in range(F + 1)]
bfs(S)

"""
풀이
수민이가 준 힌트를 보고 풀었다.
처음에 모든 경우의 수를 찾아보려했는데 U와 D가 같을 때 계속 빙빙 돌 거 같았다.
그런데 BFS를 쓰면 visitied에 방문했는지를 담아놓을 수 있으니 첫 층부터 끝층까지 방문 여부를 확인하면 된다.
"""