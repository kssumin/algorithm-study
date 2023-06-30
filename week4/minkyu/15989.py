import sys
input = sys.stdin.readline

dp = [1 for _ in range(10001)]
for i in range(2, 10001):
    dp[i] = dp[i] + dp[i - 2]
for i in range(3, 10001):
    dp[i] = dp[i] + dp[i - 3]
T = int(input())
for _ in range(T):
    num = int(input())
    print(dp[num])

"""
역시 dp는 규칙 찾기가 힘들다
처음에는 전 숫자에 1씩 더하고, 2와 3으로만 이루어진 숫자를 어떻게 더하면 될 거 같았는데 안돼서 다른 점화식을 찾았다
"""