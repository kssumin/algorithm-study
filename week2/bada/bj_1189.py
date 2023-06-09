'''
문제 : 컴백홈
난이도 : 실버1

거리가 k인 경로 구하기....

백트래킹 -> 스택
'''
import sys

d = [(0, 1), (0, -1),  (1, 0), (-1, 0)]

r, c, k = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline()) for _ in range(r)]
answer = 0


def comeback(x, y, count):
    global answer
    if count == k:
        if (x, y) == (0, c-1):
            answer += 1
    else:
        for (dx, dy) in d:
            nx = x + dx
            ny = y + dy

            if (0 <= nx < r) and (0 <= ny < c) and graph[nx][ny] == ".":
                graph[nx][ny] = "T"
                comeback(nx, ny, count + 1)
                graph[nx][ny] = "."


graph[r-1][0] = "T"
comeback(r-1, 0, 1)
print(answer)
