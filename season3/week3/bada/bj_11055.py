'''
문제 : 가장 큰 증가하는 부분 수열
난이도 : 실버2

DP가 아닐까아...

점화식을 어떻게 구해야할지 모르겠어서, LIS를 DP로 푸는 방법을 봐봤다.

길이에서 값으로만 바꾸면 풀 수 있을 것 같다!

'''
import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

dp = [0] * n

for i in range(n):
    dp[i] = nums[i]
    for j in range(i):
        if (nums[j] < nums[i]) and (dp[j] + nums[i] > dp[i]):
            dp[i] = dp[j] + nums[i]


print(max(dp))


'''
또 다른 풀이~~ 아이디어는 동일하다

for i in range(n):
    tmp = 0
    for j in range(i):
        if (nums[j] < nums[i]):
            if (dp[j] + nums[i] > dp[i]):
                tmp = max(tmp, dp[j])
    dp[i] = tmp + nums[i]
'''
