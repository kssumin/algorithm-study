import sys
from collections import deque
input = sys.stdin.readline

def rotate(gear_num, gear_direct, from_direct):
    #양쪽 진행 0
    #왼쪽 진행 1
    if from_direct >= 0 and 1 <= gear_num - 1:
        if gear[gear_num][6] != gear[gear_num - 1][2]:
            if gear_direct == 1:
                next_direct = -1
            else:
                next_direct = 1
            rotate(gear_num - 1, next_direct, 1)
    #오른쪽 진행 -1
    if from_direct <= 0 and gear_num + 1 <= T:
        if gear[gear_num][2] != gear[gear_num + 1][6]:
            if gear_direct == 1:
                next_direct = -1
            else:
                next_direct = 1
            rotate(gear_num + 1, next_direct, -1)
    # gear_direct는 톱니바퀴가 돌 방향
    # from_direct는 톱니바퀴가 주는 영향 방향
    if gear_direct == 1:
        gear[gear_num].insert(0, gear[gear_num].pop())
    elif gear_direct == -1:
        gear[gear_num].append(gear[gear_num].popleft())


T = int(input())
gear = [[]]
for _ in range(T):
    gear.append(deque(list(map(int, input().rstrip()))))
K = int(input())
for _ in range(K):
    gear_num, direct = map(int, input().split())
    rotate(gear_num, direct, 0)
result = 0
for i in range(1, len(gear)):
    if gear[i][0] == 1:
        result += 1

print(result)