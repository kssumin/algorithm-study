'''
문제 : 단지번호 붙이기(2667)
난이도 : 실버1


'''
import sys
sys.setrecursionlimit(10**7)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        global count
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


count = 0
result = 0

num = []

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            num.append(count)
            result += 1
            count = 0

print(result)
for n in sorted(num):
    print(n)
