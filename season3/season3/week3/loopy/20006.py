# 20006 랭킹전 대기열
# https://www.acmicpc.net/problem/20006

p, m = list(map(int, input().split()))

players = []
for _ in range(p):
    players.append(input().split())

rooms = []

for player in players:
    if len(rooms) == 0 :
        wating = [player]
        rooms.append(wating)
        continue

    isPassed = False
    for i, room in enumerate(rooms):
        if len(room) == m: 
            continue
        if abs(int(room[0][0]) - int(player[0])) <= 10:
            rooms[i].append(player)
            isPassed = True
            break

    if not isPassed:
        rooms.append([player])

for room in rooms:
    if len(room) == m:
        print("Started!")
        room.sort(key=lambda x: x[1])
        for player in room:
            print(' '.join(player))
    else:
        print("Waiting!")
        room.sort(key=lambda x: x[1])
        for player in room:
            print(' '.join(player))
