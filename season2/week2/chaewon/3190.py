# BJ 1918 : 뱀 / GOLD IV / 68ms

import sys
from collections import deque

# n : 보드 한 변의 길이
n = int(sys.stdin.readline().strip())

# graph : n x n 게임보드
graph = [[0] * n for _ in range(n)]

# 순서대로 아래쪽, 오른쪽, 위쪽, 왼쪽으로 이동시켜주는 좌표
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# k개의 사과
k = int(sys.stdin.readline().strip())

# graph에서 사과 위치를 2로 변경
for i in range(k):
    a, b = map(int, sys.stdin.readline().strip().split(' '))
    graph[a - 1][b - 1] = 2

# l번의 방향 전환
l = int(sys.stdin.readline().strip())

dirDict = dict()

# l번의 방향 전환을 dictionary에 저장 - key=이동시간(초): values=이동방향('L' or 'D')
for i in range(l):
    x, c = sys.stdin.readline().strip().split(' ')
    dirDict[int(x)] = c


# queue는 뱀이 graph에서 차지하고 있는 좌표를 담고 있음
queue = deque()
# 처음 뱀은 (0, 0)에 존재하므로 큐에 추가
queue.append((0, 0))

# 현재 뱀의 좌표를 x, y로 설정
x, y = 0, 0

# graph에서 뱀이 차지하는 위치를 1로 변경
graph[x][y] = 1

cnt = 0
direction = 0


def turn(alpha):
    global direction

    # 처음 뱀의 이동방향은 오른쪽
    # 이때 L 방향 변환된다면 왼쪽으로 회전하므로 graph에서 위쪽을 향해 가게 됨
    # 아래쪽, 오른쪽, 위쪽, 왼쪽
    # dx = [0, 1, 0, -1]
    # dy = [1, 0, -1, 0]
    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4


while True:
    # 뱀이 이동하므로 cnt+1
    cnt += 1

    # x와 y의 다음 좌표를 설정해줌
    x += dx[direction]
    y += dy[direction]

    # 뱀이 벽과 부딪히면 탈출
    if x < 0 or x >= n or y < 0 or y >= n:
        break

    # 뱀이 사과가 있는 칸에 도착하면
    if graph[x][y] == 2:
        # 사과를 먹으므로 사라짐 -> 뱀이 그 자리에 위치하므로 graph 값을 1로 변경
        graph[x][y] = 1

        # 뱀의 위치를 큐에 추가
        queue.append((x, y))

        # 현재 cnt가 dirDict의 key라면 = 방향 전환을 해야 한다는 뜻
        if cnt in dirDict:
            # turn함수를 호출하여 direction 값 갱신
            turn(dirDict[cnt])



    # 뱀이 빈 칸에 도착하면
    elif graph[x][y] == 0:
        # 뱀이 그 자리에 위치하므로 graph 값을 1로 변경
        graph[x][y] = 1

        # 뱀의 위치를 큐에 추가
        queue.append((x, y))

        # 사과를 먹지 않았으니 몸 길이는 유지됨
        # 이전 꼬리의 위치를 큐에서 삭제하고
        tx, ty = queue.popleft()

        # 이전 꼬리의 위치의 graph 값을 0으로 변경
        graph[tx][ty] = 0


        # 현재 cnt가 dirDict의 key라면 = 방향 전환을 해야 한다는 뜻
        if cnt in dirDict:
            # turn함수를 호출하여 direction 값 갱신
            turn(dirDict[cnt])

    else:
        break


print(cnt)


'''
NOTE:
모르겠어서 구글링으로 코드 찾아보고 한 줄씩 이해해봤다!

turn 함수를 구상해냈다는 것이 정말 신기하다
     하, 우, 상, 좌
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dx와 dy를 이루는 숫자의 순서도 맞춰줘야 한다.
만약 이게 달라지면 답 틀림...

turn 함수에서 나머지로 direction을 갱신하는 게 정말 인상적이었다
이 부분 이해를 돕기 위해 다른 예시를 더 들어보겠다!!

    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

----------------------
여러분... 제가 이 예시를 들려고 여러 상황을 가정하고 디버깅까지 직접 시행해봤는데요
뭔가 저 dx, dy의 순서가 이상한 것 같거던요ㅠ 근데 저 순서를 수정하면 틀린 걸로 나오고
지금 저대로여야 정답으로 나오는데 제가 이해를 잘못한건지... 나머지 계산을 못한건지...

제가 예시를 한번 들어볼게요

처음 graph 상에서, 뱀은 (0, 0)에서 오른쪽을 향해 가고 있죠? 그럼 다음 좌표는 (1, 0)이 되어야 하고요?

근데 직접 계산해보면 direction = 0이기 때문에, 아래와 같은 (0, 1)이 나와요..
x = x + dx[0] = 0 + 0 = 0
y = y + dy[0] = 0 + 1 = 1

계속 보다 보니까 x와 y가 바뀐.. 전치행렬 같은 느낌인건가 싶기도 한데 확 와닿지가 않네요..

이 코드 이해하신다면 코멘트 부탁드려요ㅠ

'''