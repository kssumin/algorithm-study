import sys
from itertools import accumulate
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
sum_list = list(accumulate(num_list))
for _ in range(M):
    start, end = map(int, input().split())
    start -= 1
    end -= 1
    if start == 0:
        print(sum_list[end])
    else:
        print(sum_list[end] - sum_list[start-1])