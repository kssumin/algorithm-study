# BJ 1890 : 점프 / SILVER I /

import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'rt')

n = int(sys.stdin.readline().strip())
board = []

for _ in range(n):
    # board += list(map(int, sys.stdin.readline().strip().split()))
    board.append(list(map(int, sys.stdin.readline().strip().split())))

check_board = [[0] * n for _ in range(n)]
check_board[0][0] = 1


for i in range(n):
    for j in range(n):
        if board[i][j] != 0 and check_board[i][j] != 0:
            if i + board[i][j] < n:
                check_board[i + board[i][j]][j] += check_board[i][j]
            if j + board[i][j] < n:
                check_board[i][j + board[i][j]] += check_board[i][j]

print(check_board[-1][-1])