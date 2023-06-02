import sys
input = sys.stdin.readline


def binary(st, ed):
    while st <= ed:
        mid = (st + ed) // 2
        sum_num = 0
        for num in num_list:
            if num > mid:
                sum_num += mid
            else:
                sum_num += num
        if sum_num > M:
        # mid가 작아져야함
            ed = mid - 1
        else:
            st = mid + 1
    return ed


N = int(input())
num_list = list(map(int, input().split()))
num_list.sort(reverse=True)
M = int(input())
if sum(num_list) <= M:
    print(num_list[0])
else:
    print(binary(1, num_list[0]))

"""
풀이
문제 범위를 보니깐 이진 탐색을 써야될 것 같아서 이진 탐색을 쓰게 됐다

이진 탐색을 할 때 최소값부터 최대값까지 탐색하게 해서 최솟값과 최댓값이 같은 때를 고려하지 않아서 틀렸다.
또 6번째줄에서 <=가 아니라 <를 해서 틀렸었다.
"""