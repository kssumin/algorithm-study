import sys; input = sys.stdin.readline
sudoku = [list(map(int. input().split())) for i in range(9)]

def find_row(a, N):
    for i in range(9):
        if N == sudoku[a][i]:
            return False
    return True

def find_col(b, N):
    for i in range(9):
        if N  == sudoku[b][i]:
            return False
    return True

def find_squ(x, y, N):
    for i in range(3):
        for j in range(3):
            if N == sudoku[y // 3 * 3 + i][x // 3 * 3 + j]:
                return False
    return True

