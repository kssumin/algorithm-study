from collections import deque
import sys
#import numpy as np
input = sys.stdin.readline


def game():
    direct = 'R'
    x, y = (0, 0)
    graph[x][y] = 'O'
    result = 0
    # 몇번째에 방향을 바꿀지, 머리를 틀 방향
    move, op = move_list.popleft()
    snake = deque()
    snake.append((x, y))
    while 1:
        # print(np.array(graph))
        # print("----------------------------------------------------------------")
        # dx, dy == 나아갈 방향의 x값, y값
        dx, dy = x + direct_dict[direct][0], y + direct_dict[direct][1]
        snake.append((dx, dy))
        if dx >= N or dy >= N or dx < 0 or dy < 0:
            print(result + 1)
            break
        elif graph[dx][dy] == 'O':
            print(result + 1)
            break
        # 사과를 만나면 뱀의 꼬리를 pop 하지 않는다
        if graph[dx][dy] == '*':
            pass
        else:
            # 나머지는 뱀의 꼬리를 pop 한다
            x, y = snake.popleft()
            graph[x][y] = 'X'
        graph[dx][dy] = 'O'
        x, y = dx, dy
        result += 1
        # 방향 전환할 때가 되었다면 전환
        if move == result:
            direct = turn_direct(direct, op)
            if move_list:
                move, op = move_list.popleft()

    return


def turn_direct(now_direct, op):
    direct_list = list(direct_dict)
    index = direct_list.index(now_direct)
    if op == 'D':
        index += 1
    elif op == 'L':
        index -= 1

    if index < 0:
        index = 3
    if index == 4:
        index = 0
    return direct_list[index]

# 보드 크기
N = int(input())
# 사과 개수
K = int(input())
graph = [['X' for _ in range(N)] for _ in range(N)]
for i in range(K):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x][y] = '*'
# 방향 변환 횟수
L = int(input())
move_list = deque()
for i in range(L):
    X, C = map(str, input().rstrip().split())
    X = int(X)
    # 몇번째에 변환하는지, 무슨 방향인지
    move_list.append((X, C))

# 뱀 머리 방향
direct_dict = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}

game()

"""
맨날 '설마 이렇게까지 해야되나' 라고 생각되면 그걸 해야한다.... 
그냥 코드를 짜다가 필요할 거 같은 변수 하나 하나씩 추가하고 그에 맞춰서 조건도 추가해주니 잘 풀렸다.
이 문제는 뱀의 머리랑 꼬리가 중요하다. 언뜻 보면 뱀 전체가 움직여야될 거 같지만 사실 뱀의 머리와 꼬리만 움직인다.
그래서 각각을 잘 다루면 코드가 짜진다.

풀이
일단 뱀의 진행 방향들을 오른쪽부터 시계방향대로 direct_dict 에 저장해둔다. 뱀의 진행 방향에 따라 원래 좌표에 더해주는 값이 바뀌기 때문이다. 현재 진행 방향은 direct 에 저장해둔다.
그리고 뱀이 몇 초에 머리를 트는지 알아야 하므로 입력 된 것들은 move_list 에 담아두고 내가 현재 몇 초인지 나타내는지도 result 에 저장해둔다.
snake 에는 뱀을 나타낸다. 뱀이 벽을 만나거나 자신을 만나면 result +1 을 출력하고 마친다.
만약 사과를 만난다면 뱀의 꼬리를 pop 하지 않고 그냥 길을 간다면 뱀의 꼬리를 pop 한다.
뱀의 머리를 틀 때가 되었다면 뱀의 머리를 튼다.

뱀의 머리를 트는 함수를 따로 만들었는데, 오른쪽부터 시계방향대로 direct_dict 에 담아두었기 떄문에 인덱싱을 위해 list 로 형변환 해주어 direct_list 에 저장한다.
만약 D 를 만나면 index 에 1을 더해주고 L 을 만나면 1 을 빼주면 된다. (시계방향대로 담아둔 이유)
D 를 만났을 때나 L 을 만났을 때 index 가 -1이나 4가 될 가능성이 있는데 -1이라면 direct_list 의 맨 마지막 값, 4라면 맨 앞의 값을 나타내니 인덱스를 바꿔주면 된다.
"""