'''
/*문제 정보 */
15662번 - 톱니바퀴 (2)
난이도 - 골드 5
/*풀이 방법 */
https://velog.io/@i_am_developer/%EB%B0%B1%EC%A4%80python15662-%ED%86%B1%EB%8B%88%EB%B0%94%ED%80%B42
리뷰 했습니다.
'''

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())    # 톱니바퀴의 개수
wheel = [deque(map(int, input().strip()))for _ in range(T)] # 톱니바퀴 상태

def move(n,d):
    global cur_right, cur_left, wheel
    origin_dir = d

    for i in reversed(range(n)):    # 왼쪽의 톱니바퀴
        if wheel[i][2] != cur_left:
            cur_left = wheel[i][6]
            wheel[i].rotate(d*-1)
            d *= -1
        else:
            break
    d = origin_dir
    for i in range(n+1, T):          # 오른쪽의 톱니바퀴
        if wheel[i][6] != cur_right:
            cur_right = wheel[i][2]
            wheel[i].rotate(d*-1)
            d *= -1
        else:
            break

K = int(input())                    # 회전 횟수

for _ in range(K):
    n,d = map(int, input().split())   # 횟수(n)와 방향(d)
    cur_left, cur_right = wheel[n-1][6], wheel[n-1][2]    # 톱니바퀴 12시 방향이 인덱스 0이니 각각 왼쪽, 오른쪽 맞닿는 인덱스 번호
    wheel[n-1].rotate(d)   # 파이썬 ratate 함수 사용
    move(n-1, d)           # 왼쪽, 오른쪽 톱니바퀴 옮겨주는 함수

print(sum([1 if wheel[0] else 0 for delta, wheel in enumerate(wheel)]))
'''
/*오답 노트*/
1. 톱니바퀴가 움직이는 것에 따라 위치를 조정해줘야 하기 때문에 자료구조 문제라고 생각했다.
2. 예시를 보고 문제를 이해하는데 완벽히 이해가 되지 않았다.
3. 조건에 따라 여러 바퀴의 위치를 바꿔줄 방법이 쉽게 떠오르지 않았다.
/*느낀 점*/
파이썬은 여러 라이브러리, 함수 종류가 많은 것 같다. rotate 없이 조건문, 반복문으로
작성했더라면 더 길고 복잡해졌을 것이다.
'''