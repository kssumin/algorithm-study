import sys
input = sys.stdin.readline


T = int(input())
dp = [0 for _ in range(11)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T):
    n = int(input())
    print(dp[n])

"""
풀이
첫 번째 풀이
dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4] ··· + dp[1]을 했는데 이상하게 출력된다.
그래서 다른 풀이를 찾다가 문제가 dp라서 점화식이 어떻게 되는지 찾다가 dp[i] = dp[i-1] + dp[i-2] + dp[i-3]라는 규칙을 알아냈다.
왜 그런지는 모르겠다. 주제가 dp라는 걸 알아야만 이렇게 풀 수 있기 때문에 이렇게 풀고 마는거보단 저 규칙이 왜 나왔는지 찾아봐야겠다. 

첫 번째 생각보다 조금 더 생각했으면 풀 수 있었다. ㅠㅠ
dp[i] = dp[i-1]에 1씩 더하면 i를 만들 수 있고 마찬가지로 dp[i-2]는 2, dp[i-3]은 3을 더하면 만들 수 있기 때문에 위의 점화식이 답이였다.
"""