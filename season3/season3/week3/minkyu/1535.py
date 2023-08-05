import sys
input = sys.stdin.readline


N = int(input())
L = [0] + list(map(int, input().split()))
J = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(100)]for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(100):
        if L[i] <= j:
            dp[i][j] = max(J[i] + dp[i-1][j-L[i]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])

"""
풀이
dp로 풀긴 풀었는데 아직도 헷갈린다.

우선 도저히 못 풀겠어서 무슨 알고리즘으로 풀어야하는지 봤다.
배낭 문제라고 돼 있길래 다른 배낭 문제 풀이를 봤다.
12865번 풀이를 보고 어떻게 풀지 알았는데도 여전히 어렵다.
"""
