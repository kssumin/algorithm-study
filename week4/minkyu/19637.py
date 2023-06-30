import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name_list = []
for _ in range(N):
    name, level = input().split()
    name_list.append((int(level), name))
for _ in range(M):
    user_level = int(input())
    start = 0
    end = len(name_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if user_level > name_list[mid][0]:
            start = mid + 1
        else:
            end = mid - 1
    print(name_list[start][1])

"""
문제에서 범위를 보고 이분탐색을 떠올렸지만 오랜만에 풀어서 그런지 헷갈렸다.
처음 풀 땐 그냥 순차 탐색을 했다가 틀려서 이분탐색으로 풀었다.
"""
