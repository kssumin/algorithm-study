'''
/*문제 정보 */
3190번 - 뱀
난이도 - 골드 4
/*결과*/
메모리 - 34192 KB
시간 - 68 ms
코드 길이 - 1344 B
/*풀이 방법 */
문제의 조건에 맞춰 입력 받아준 뒤 deque로 뱀의 이동을 나타냈다.
문제의 조건에 따라 입력 받는 값을 설정하고, 조건에 따라 뱀의 이동을 나타냈다.
'''
import sys
input = sys.stdin.readline

from collections import deque

n = int(input())  # 보드의 크기
k = int(input())  # 사과의 개수

graph = [[0] * n for _ in range(n)]   # 맵을 다 0으로 시작

for i in range(k):                 # 사과 좌표 입력
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1            # 그래프에 넣어줌

l = int(input())  # 뱀의 방향 변환 횟수
move = {}   # 뱀 방향 정보 저장 딕셔너리
for i in range(l):
    x, c =map(str, input().split())    # 뱀의 방향 정보 입력
    move[int(x)] = c

#우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y, d = 0, 0, 0  # 뱀의 초기 위치, 초기 방향

snake = deque([])
time = 0  # 시간

while True:
    snake.append((x, y))  # 뱀 현재 위치 입력 (0,0)
    time += 1    # 매번 움직일 때마다 1초 증가

    x += dx[d]
    y += dy[d]

    if x < 0 or x >= n or y < 0 or y >= n or graph[x][y] == 2:
        break                   # 벽에 닿거나 자신의 몸에 닿으면

    if not graph[x][y]:
        i, j = snake.popleft()   # 사과가 없다면 꼬리 없애주고
        graph[i][j] = 0

    graph[x][y] = 2   # 뱀의 몸 위치는 2로 넣어주기

    if time in move:    # 각도를 변하는 시간이 오면

        if move[time] == 'D':   # 시계 방향으로 돌때
            d = (d+1) % 4

        else:
            d = (d-1) % 4


print(time)


'''
/*오답 노트*/
/*느낀 점*/
1. 처음에 아래와 같이 이동 순서를 아무렇게 넣었더니 작동은 되나 답이 잘못 나왔다..
dx = [0, 0, 1, -1] 다시 좌우상하로 순서르 바꿔서 넣었더니 제대로 작동했다.
dy = [1, -1, 0, 0]

2.  풀이 방법에는 간단하게 적었지만, 입력 받아주는 것 설정도 다른 문제에 비해 
    힘들었고, 뱀의 이동을 코드로 나타내는게 어려워서 인터넷의 도움을 요청했다.
    다른 문제였으면 dx,dy도 아무렇게나 놓아도 되는데 이 문제는 그렇지 않았다 ㅠㅠ
'''