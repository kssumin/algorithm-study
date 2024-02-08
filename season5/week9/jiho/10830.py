import sys; input = sys.stdin.readline

size, square = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(size)]

def mul(matrix1, matrix2):
    x = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                x[i][j] += matrix1[i][k] * matrix2[k][j] % 1000
    return x

def DPow(matrix, square):
    if square == 1:
        return matrix
    else:
        tmp = DPow(matrix, square // 2)
        if square % 2 == 0:
            return mul(tmp, tmp)
        else:
            return mul(mul(tmp, tmp), matrix)

res = DPow(matrix, square)
for i in range(size):
    for j in range(size):
        res[i][j] = res[i][j] % 1000

for i in res:
    print(*i)