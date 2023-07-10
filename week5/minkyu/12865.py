import sys
input = sys.stdin.readline


N, K = map(int, input().split())
dp = [[[0,0], [0 for _ in range(K + 1)]]]
for _ in range(N):
    dp.append([list(map(int, input().split())), [0 for _ in range(K + 1)]])

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if dp[i][0][0] > j:
            dp[i][1][j] = dp[i-1][1][j]
        else:
            dp[i][1][j] = max(dp[i-1][1][j], dp[i][0][1] + dp[i-1][1][j-dp[i][0][0]])
print(dp[-1][1][-1])


"""
3주차 문제 1535번을 풀 때 냅색 알고리즘을 이용한 기억이 있었는데 한번밖에 풀어보질 못해서 그런지
대충 기억나서 아래 사이트를 참고해서 다시 작성했다..
어렵다... 이해는 가는데 외워야 풀 수 있을 것 같다.
https://gsmesie692.tistory.com/113
"""