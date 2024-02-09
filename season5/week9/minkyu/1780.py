import sys
input = sys.stdin.readline


def cut(x, y, cnt):
    flag = graph[x][y]
    for i in range(x, x+cnt):
        for j in range(y, y+cnt):
            if graph[i][j] != flag:
                for k in range(3):
                    for l in range(3):
                        cut(x + k * cnt // 3, y + l * cnt // 3, cnt // 3)
                return
    if flag == -1:
        answer[0] += 1
    elif flag == 0:
        answer[1] += 1
    else:
        answer[2] += 1


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = [0,0,0]
cut(0, 0, N)
print(*answer, sep="\n")