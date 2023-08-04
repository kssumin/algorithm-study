import sys
from itertools import combinations
input = sys.stdin.readline
INF = sys.maxsize


def get_sum(chicken_set):
    sum = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in chicken_set:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        sum += temp
    return sum


N, M = map(int, input().split())
graph = []
house = []
chicken = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            house.append([i, j])
        elif row[j] == 2:
            chicken.append([i, j])
    graph.append(row)

chicken_combi = list(combinations(chicken, M))

result = INF
for chicken_set in chicken_combi:
    result = min(result, get_sum(chicken_set))
print(result)

"""
첫 번째 풀이
폐업시키지 않을 치킨 집의 우선순위를 두 개를 두었다.
1. 선택된 집들의 개수
2. 집들과의 거리 합
첫 번째로 선택된 집들의 개수가 많은 순으로 정렬하고 그 개수가 같다면 집들의 거리 합이 작은 순으로 정렬했다.
저번에 바다가 알려준 코드를 활용했다.
웬만한 테스트 케이스들은 통과하는데 아래 케이스는 통과하지 못한다.
2100012
0001000
0000000
0002000
0000000
0000000
2100012
처음에 브루트 포스로 풀려고 했을 때 경우의 수가 너무 많이 나와서 안했는데 알고보니 계산을 잘못했다.
최대로 계산해야할 때가 13C6인데 100C13으로 계산했었다. 왜그랬을까
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
# house = [[x, y]]
house = []
# chicken = [[x, y, 선택된 집의 개수, 집들까지 거리의 합]]
chicken = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            house.append([i, j])
        elif row[j] == 2:
            chicken.append([i, j, 0, 0])
    graph.append(row)

for i in range(len(house)):
    distance_list = []
    for j in range(len(chicken)):
        distance = abs(house[i][0] - chicken[j][0]) + abs(house[i][1] - chicken[j][1])
        distance_list.append([distance, j])
        chicken[j][3] += distance
    chicken_index = min(distance_list)[1]
    chicken[chicken_index][2] += 1
    house[i].append(chicken_index)

chicken.sort(key= lambda x:(-x[2],x[3]))
while len(chicken) > M:
    close_x, close_y, _, _ = chicken.pop()
    graph[close_x][close_y] = 0
result = 0
for i in range(len(house)):
    distance_list = []
    for j in range(len(chicken)):
        distance = abs(house[i][0] - chicken[j][0]) + abs(house[i][1] - chicken[j][1])
        distance_list.append(distance)
    result += min(distance_list)
print(result)
"""