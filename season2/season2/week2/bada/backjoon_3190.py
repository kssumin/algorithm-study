'''
문제 : 3190번 뱀
난이도 : 골드4


'''
import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[0]*n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

k = int(sys.stdin.readline())
for _ in range(k):
    c, r = map(int, sys.stdin.readline().split())
    graph[c-1][r-1] = 1

l = int(sys.stdin.readline())
dirs = {}
for _ in range(l):
    x, c = sys.stdin.readline().rstrip().split()
    x = int(x)
    dirs[int(x)] = c

direction = 0
count = 0
snack = deque()
snack.appendleft([0, 0])
while snack:
    tail = snack.pop()
    tmp_x = tail[0] + dx[direction]
    tmp_y = tail[1] + dy[direction]
    tmp = [tmp_x, tmp_y]
    count += 1

    if 0 <= tmp_x < n and 0 <= tmp_y < n and tmp not in snack:
        if graph[tmp_x][tmp_y] == 1:
            snack.appendleft(tmp)
            snack.append(tail)
        else:
            snack.appendleft(tmp)
        
        
        if count in dirs:
            if dirs[count] == "L":
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4

    else:
        break
    
print(count)

# 시간이 부족해용,, 제대로 풀어서 다시 제출할게용 ㅠ 벌금은 내겠숩니다