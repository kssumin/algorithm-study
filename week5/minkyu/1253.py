import sys
input = sys.stdin.readline
INF = sys.maxsize


def is_good(index):
    start = 0
    end = N - 1
    if index == 0:
        start += 1
    elif index == N - 1:
        end -= 1
    while 1:
        if (not ((0 <= start < N) and (0 <= end < N))) or (index == start) or (index == end) or (start == end):
            return False
        # 어떤 수가 작을 때
        if num_list[start] + num_list[end] > num_list[index]:
            end -= 1
            if index == end:
                end -= 1
        elif num_list[start] + num_list[end] < num_list[index]:
            start += 1
            if index == start:
                start += 1
        else:
            return True


N = int(input())
num_list = sorted(list(map(int, input().split())))
result = 0
for i in range(N):
    if is_good(i):
        result += 1
print(result)

"""
처음에 문제를 잘못 이해했다.
문제에서는 "N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있으면"이라고 되어 있는데
나는 어떤 수를 포함해서 그 어떤 수를 만들 수 있는지도 포함했다.

그래서 수정해서 풀어봤는데도 시간초과가 뜬다.
탐색 위치를 start, end = index - 1, index + 1에서 시작하면 시간초과가 뜨고, start, end = 0, N - 1에서 하면 통과한다. 왜지...?
"""