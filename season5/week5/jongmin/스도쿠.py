# 스도쿠 문제
# 가로,세로,3x3에 해당하는 영역 1~9가 모두 1개씩 -> 합이 45로 일정
# 입력 : 9x9에 해당하는 빈 칸이 있는 스도쿠 판(빈 칸은 0)
# 출력 : 빈 칸이 채워진 스도쿠 판

import sys

# 스도쿠 탐색
# 세로의 합
# 가로의 합
# 3x3의 합
def dfs(row=0):
    if row>=9:
        return
    # 가로를 탐색
    for col in range(0,9):
        # 비었으면 1부터 9까지 포함 안되어 있는 수를 넣음
        if board[row][col]==0:
            for s in range(1,10):
                if s not in set(board[row]):
                    board[row][col] = s
                    print(f"############ {row}행 {col}열 ############")
                    for i in board:
                        print(i)
                    if sum(board[row])==45: dfs(row+1)
                    else: dfs(row)
                    # 가로 줄 한 줄을 다 채웠을 때, 스도쿠인지 아닌지 판별
                    if not is_Latin_square(row,col):
                        board[row][col] = 0
                        print(f"############ {row}행 {col}열 ############")
                        for i in board:
                            print(i)

def is_Latin_square(row,col):
    # 가로,세로,3x3의 합이 45가 되어야 함
    rstart_3 = (row//3)*3
    rend_3 = rstart_3 + 3
    cstart_3 = (col//3)*3
    cend_3 = cstart_3 + 3

    sum_3_3 = 0
    sum_col = sum([board[i][col] for i in range(9)])
    sum_row = sum(board[row])
    for i in range(rstart_3,rend_3):
        for j in range(cstart_3,cend_3):
            sum_3_3 += board[i][j]

    return True if sum_3_3==sum_col==sum_row==45 else False
###################

board = []
visited = []
for _ in range(9):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

dfs()

print("################")
for i in board:f
    print(i)