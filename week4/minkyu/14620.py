from itertools import combinations
import sys
input = sys.stdin.readline

def get_cost(dot1, dot2, dot3):
    tmp = [(0,0), (1,0), (-1,0), (0,1), (0,-1)]
    dot_set = set()
    for x, y in dot1, dot2, dot3:
        for dx, dy in tmp:
            dot_set.add((x + dx, y + dy))
    if len(dot_set) != 15:
        return False
    cost = 0
    for x, y in list(dot_set):
        cost += graph[x][y]
    total_cost.append(cost)

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
seed = [(x, y) for x in range(1, N-1) for y in range(1, N-1)]
total_cost = []
for a, b, c in combinations(seed, 3):
    get_cost(a, b, c)
print(min(total_cost))
"""
처음에 5개의 땅값의 합이 가장 적은 순서대로 3번 선택하는 방법을 썼는데 틀렸다.
각각 합이 적은 순서대로 선택해야하는 것이 아니라 15개의 땅 값의 합이 적은 것을 찾아내야 한다..
그럼 모든 경우의 수를 해봐야한다. 이 방법은 시간이 많이 걸릴 거 같았는데 통과한다.
"""