# BJ 1912 : 연속합 / SILVER II /

import sys
sys.stdin = open('input.txt', 'rt')

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))

result = [0]
sum_nums = 0
sum_list = [0]

def dp():
    global result
    global sum_nums
    global sum_list
    for i in range(0, n-2):
        sum_nums += nums[i]
        sum_list.append(sum_nums)
        if max(sum_list) <= result[-1]:
            continue
        else:
            result.append(max(sum_list))
        dp
