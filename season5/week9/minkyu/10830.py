import sys
input = sys.stdin.readline


def solution(A, B):
    if B == 1:
        return A
    else:
        op = solution(A, B // 2)
        if B % 2 == 0:
            return mul(op, op)
        else:
            return mul(mul(op, op), A)


def mul(mat1, mat2):
    result_mat = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result_mat[i][j] += mat1[i][k] * mat2[k][j] % 1000
    return result_mat


N, B = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

result = solution(graph, B)
for i in range(N):
    for j in range(N):
        print(result[i][j] % 1000, end=' ')
    print()