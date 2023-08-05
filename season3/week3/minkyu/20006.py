import sys
input = sys.stdin.readline

p, m = map(int, input().split())
room_list = []
for j in range(p):
    level, name = input().split()
    level = int(level)
    if j == 0:
        room_list.append([(level, name)])
        continue
    for i in range(len(room_list)):
        if room_list[i] and room_list[i][0][0] - 10 <= level <= room_list[i][0][0] + 10 and len(room_list[i]) < m:
            room_list[i].append((level, name))
            break
    else:
        room_list.append([(level, name)])

for room_num in room_list:
    room_num.sort(key=lambda x:x[1])
    if len(room_num) == m:
        print("Started!")
    else:
        print("Waiting!")
    for level, name in room_num:
        print(level, name)

"""
풀이
그냥 무슨 알고리즘을 쓰진 않고 조건대로 식을 만들어주었더니 풀렸다.

처음에 방이 꽉 차지 않으면 waiting을 출력하는 조건을 읽지 않았다.
그 다음에는 사전순으로 정렬하는 조건을 읽지 않았다...
문제를 잘 읽자...
"""