# 7490 0만들기
# https://www.acmicpc.net/problem/7490

N = int(input())

result = []
def findAllPaths(i, M, str):
    if i >= M:
        ns = ''.join(str.split(' '))
        if eval(ns) ==0:
            result.append(str)
        return
    next = i + 1
    findAllPaths(next, M, str + f" {next}")
    findAllPaths(next, M, str + f"+{next}")
    findAllPaths(next, M, str + f"-{next}")

for i in range(N):
    M = int(input())
    result = []
    findAllPaths(1, M, '1')
    for j in result:
        print(j)
    print()