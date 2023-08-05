# 1189 컴백홈
# https://www.acmicpc.net/problem/1189

R, C, K = list(map(int, input().split()))
paths = [list(input()) for _ in range(R)]
results = []
y = R - 1
x = 0


def findAllPaths(x, y, dep):
    if y == 0 and x == C:
        results.append(dep)
        # for i in paths:
        #     print(i)
        # print("------------------")
    if y == R or x == C or y == -1 or x == -1:
        return
    if paths[y][x] == ".":
        dep += 1
        paths[y][x] = "="
        findAllPaths(x, y + 1, dep)
        findAllPaths(x + 1, y, dep)
        findAllPaths(x, y - 1, dep)
        findAllPaths(x - 1, y, dep)
        paths[y][x] = "."


findAllPaths(x, y, 0)

count = 0
for i in results:
    if i == K:
        count += 1

# print(results)

print(count)
