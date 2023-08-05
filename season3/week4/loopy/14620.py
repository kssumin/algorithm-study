# [14620번](https://www.acmicpc.net/problem/14620) 꽃길 (실버2)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
check_board = [[False] * N for _ in range(N)]

def check(x, y):
  return x <= 0 or x  >= N - 1 or y <= 0 or y  >= N - 1

def board_checker(x, y):
  global check_board
  return check_board[x][y] or check_board[x + 1][y] or check_board[x - 1][y] or check_board[x][y + 1] or check_board[x][y - 1]

def get_sum(x, y):
  global board
  return board[x - 1][y] + board[x + 1][y] + board[x][y - 1] + board[x][y + 1] + board[x][y]

min_value = 100000

def dfs(count, sum_value):
  global min_value, check_board

  if count == 3:
    min_value = min(min_value, sum_value)
    return
  
  for i in range(0, N):
    for j in range(0, N):
      if not check(i, j) and not check_board[i][j] and not board_checker(i, j):
        check_board[i][j] = True
        check_board[i+1][j] = True
        check_board[i-1][j] = True
        check_board[i][j+1] = True
        check_board[i][j-1] = True

        dfs(count + 1, sum_value + get_sum(i, j))

        check_board[i][j] = False
        check_board[i+1][j] = False
        check_board[i-1][j] = False
        check_board[i][j+1] = False
        check_board[i][j-1] = False

dfs(0, 0)

print(min_value)