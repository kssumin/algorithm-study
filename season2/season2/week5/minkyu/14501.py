import sys
input = sys.stdin.readline

N = int(input())
list_T = [0]
list_P = [0]
dp = [0] * (N + 1)
for i in range(N):
    T, P = map(int, input().split())
    list_T.append(T)
    list_P.append(P)

for i in range(1, N + 1):
    end_date = i + list_T[i] - 1
    if end_date <= N:
        dp[end_date] = max(dp[end_date], dp[i - 1] + list_P[i])
    dp[i] = max(dp[i - 1], dp[i])
print(max(dp))

"""
풀이
dp로 풀었다
처음에 17번째줄을 작성하지 않아서 틀렸는데 작성하지 않으면 Ti가 1이 아닐 때 dp[i]가 할당이 안 될 수 있다.
"""