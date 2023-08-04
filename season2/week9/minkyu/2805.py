import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree_list = list(map(int, input().split()))
tree_list.sort(reverse=True)
# 20 17 15 10
start, end = 0, tree_list[0]
while end >= start:
    result = 0
    mid = (start + end) // 2
    for num in tree_list:
        if num > mid:
            result += num - mid
        else:
            break
    if result >= M:
        start = mid + 1
    elif result < M:
        end = mid - 1

print(end)

"""
처음에 왜 이분탐색을 써야하는지 몰랐다.
그런데 N값이 100만으로 엄청 큰 숫자여서 이분탐색을 쓰지 않으면 시간이 엄청나게 오래 걸린다.

찾고자 하는 값이 없을 때 값을 찾는 것이 어려웠다...
"""