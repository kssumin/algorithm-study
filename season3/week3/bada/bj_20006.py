'''
문제 : 랭킹전 대기열
난이도 : 실버2

room들을 담는 2차원 리스트 생성
각 room list에는 player 정보가 담겨져 있음
'''
import sys

p, m = map(int, sys.stdin.readline().split())
room_list = []


def enter_room(info):
    for room in room_list:
        if len(room) >= m:
            continue
        elif (room[0][0] - 10 <= info[0] <= room[0][0] + 10):
            room.append(info)
            return
    room_list.append([info, ])
    return


for _ in range(p):
    l, n = sys.stdin.readline().split()
    l = int(l)
    enter_room((l, n))

for room in room_list:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    room.sort(key=lambda x: x[1])
    for player in room:
        print(f"{player[0]} {player[1]}")
