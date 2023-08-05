'''
/*문제 정보 */
20006번 - 랭킹전 대기열
난이도 - 실버 2
/*풀이 방법 */
https://velog.io/@meganatc7/%EB%B0%B1%EC%A4%80-20006.-%EB%9E%AD%ED%82%B9%EC%A0%84-%EB%8C%80%EA%B8%B0%EC%97%B4-Python
코드 리뷰 했습니다.

'''
import sys
input = sys.stdin.readline

P, M = map(int, input().split())
rooms = []

# 각각의 플레이어를 입력 받아 방에 넣어주기
for p in range(P):
    l, n = input().split()
    # 최초 입력된 플레이어
    if not rooms:
        rooms.append([[int(l), n]])
        continue

    # 방에 들어갔는지 확인 하는 flag변수
    enter = False
    # 각 방을 돌면서
    for room in rooms:
        # 조건에 합당하면 넣어주기
        if len(room) < M and room[0][0] - 10 <= int(l) <= room[0][0] + 10:
            room.append([int(l), n])
            enter = True
            break
    # 못들어갔으면 새로운 방을 파서 넣어주기
    if not enter:
        rooms.append([[int(l), n]])

# 이름 기준 정렬
for room in rooms:
    room.sort(key=lambda x: x[1])

# 정원 수에 따라 출력
for room in rooms:
    if len(room) == M:
        print('Started!')
    else:
        print('Waiting!')
    for lv, name in room:
        print(lv, name)
'''
/*오답 노트*/
/*느낀 점*/
내가 풀지 못했던 이유는
1. room 리스트에 플레이어의 이름과 레벨을 저장하는 방식을 떠올리지 못했고
2. 조건에 따라 새로운 방을 만드는 방법을 떠올리지 못했다. false / true 방식을 알게 되었다.
3. 매번 코드 리뷰하면서 느끼지만 lambda 함수나 리스트 [:] 식의 표현 방식을 익혀야겠다.
'''
