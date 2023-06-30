'''
1,2,3 더하기 4


4 = 1+3, 2+2

2 + 1 + 1
1 + 2 + 1

DP인건 알겠어, 근데 겹치는 건 어떻게 해결?


'''
import sys

dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]

for i in range(3, 10001):
    dp[i] += dp[i - 3]

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp[n])
