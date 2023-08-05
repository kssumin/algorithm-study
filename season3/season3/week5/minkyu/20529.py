from itertools import combinations
import sys

input = sys.stdin.readline
INF = sys.maxsize

personality_list = sorted(
    ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ',
     'ENFJ', 'ENTJ'])
personaltiy_dict = {}
for i in range(16):
    personaltiy_dict[personality_list[i]] = i
distance_list = [[0 for _ in range(16)] for _ in range(16)]
for i in range(16):
    for j in range(i + 1, 16):
        distance = 0
        for k in range(4):
            if personality_list[i][k] != personality_list[j][k]:
                distance += 1
        distance_list[i][j], distance_list[j][i] = distance, distance

T = int(input())
for _ in range(T):
    N = int(input())
    tmp_list = list(input().split())
    min_distance = INF
    count_dict = {}
    for i in range(len(tmp_list)):
        count_dict.setdefault(tmp_list[i], 0)
        count_dict[tmp_list[i]] += 1
        if count_dict[tmp_list[i]] >= 3:
            min_distance = 0
            break

    if min_distance != 0:
        for combi in combinations(tmp_list, 3):
            total_distance = 0
            for combi2 in combinations(combi, 2):
                p1, p2 = combi2
                total_distance += distance_list[personaltiy_dict[p1]][personaltiy_dict[p2]]
            min_distance = min(min_distance, total_distance)
    print(min_distance)

"""
처음 문제를 보고 메모리 여유가 많아서 그냥 브루트 포스로 풀면 되겠다 하고 모든 경우의 수를 다 집어넣었다.
그런데 시간 초과가 떴다. 거리를 계산할 때 시간이 오래 걸리는 것 같다고 생각해서 mbti를 사전순으로 정렬한뒤 숫자를 부여하고
distance_list에 각각의 거리를 저장해주었다. 그런데도 시간초과가 떴다.
알고보니 3개 이상의 중복된 값이 있을 땐 계산할 필요도 없이 0을 출력하면 됐다.
따라서 아무리 많아도 48개의 값을 계산하면 돼서 시간이 그렇게 많이 걸리지 않는다.
"""