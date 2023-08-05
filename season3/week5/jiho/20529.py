# 20529
def DFS(arr, i, K):
    global cache
    result = 987654321
    cache[i] = 1
    arr.append(graph[i])
    K += 1
    if K == 3:
        result = min(result, check(arr))
    else:
        for j in range(i, N):
            if cache[j] == 0:
                result = min(result, DFS(arr, j, K))
    arr.pop()
    K -= 1
    cache[i] = 0
    return result


def check(arr):
    out = 0
    one = arr[0]
    two = arr[1]
    three = arr[2]
    for j in range(0, 4):
        if one[j] != two[j]:
            out += 1
        if two[j] != three[j]:
            out += 1
        if three[j] != one[j]:
            out += 1

    return out


T = int(input())

for i in range(0, T):
    N = int(input())
    graph = [0] * N
    cache = [0] * N
    aa = 987654321
    alist = list(map(str, input().split()))
    if N >= 33:
        print(0)
    else:
        for i in range(0, N):
            graph[i] = alist[i]
        for i in range(0, N):
            aa = min(aa, DFS([], i, 0))
        print(aa)
