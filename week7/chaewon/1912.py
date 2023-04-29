# BJ 1912 : 연속합 / SILVER II / 96ms

import sys

sys.stdin = open('input.txt', 'rt')

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))


dp = [0] * n        # nums[i]까지 고려했을 때 최대 연속합
dp[0] = nums[0]
for i in range(1, n):
    dp[i] = max(nums[i], dp[i-1]+nums[i])       # arr[i] 혹은 이전 최대 연속합+arr[i]
print(max(dp))

'''
NOTE:

점화식을 세워서 푸는 문제는 정말 어려운 것 같다... 수학적 사고력을 길러야 하나 보다...
못 풀어서 구글링해봤다
어떻게 이렇게 간단하게 푸는건지 ... ???

DP는 정말 연습을 많이 해봐야하는 것 같다

'''