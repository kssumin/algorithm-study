'''
문제 : 1904번
난이도 : 실버3

DP[n]은 DP[n-1]에 '1' 붙이는 경우와 DP[n-2]에 '00'를 붙이는 경우를 합한 결과
즉, DP[n] = DP[n-1] + DP[n-2]

문제 잘 읽자~
-> 15746으로 나눈 나머지를 출력한다.
'''
import sys

n = int(sys.stdin.readline())

dp = [0] * 1000001
dp[0] = 1
dp[1] = 2

for k in range(2, n):
    dp[k] = (dp[k-1] + dp[k-2]) % 15746
print(dp[n-1])
