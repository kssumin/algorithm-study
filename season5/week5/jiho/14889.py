import sys
input = sys.stdin.readline

def backtracking(play, idx):
    global minimum
    if play == N // 2:
        exp1, exp2 = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    exp1 += player[i][j]
                elif not visited[i] and not visited[j]:
                    exp2 += player[i][j]
        minimum = min(minimum, abs(exp1 - exp2))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            backtracking(play + 1, i + 1)
            visited[i] = False

N = int(input())
player = [list(map(int, input().split())) for i in range(N)]
visited = [False for i in range(N)]
minimum = sys.maxsize
backtracking(0, 0)
print(minimum)
