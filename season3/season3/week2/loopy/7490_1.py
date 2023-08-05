# 7490 0만들기
# https://www.acmicpc.net/problem/7490

N = int(input())

result = []
def findAllPaths(i, M, str, value, sign):
    if i >= M:
        if value == 0:
            result.append(str)
        return
    next = i + 1
    findAllPaths(next, M, str + f" {next}", value + sign * (i * 9 + next), sign)
    findAllPaths(next, M, str + f"+{next}", value + next , 1)
    findAllPaths(next, M, str + f"-{next}", value - next , -1)

for i in range(N):
    M = int(input())
    result = []
    findAllPaths(1, M, '1', 1, 1)
    for j in result:
        print(j)
    print()