'''
문제 : 점프 (1890)
난이도 : 실버1

하쉬,,, 이게 디피야?

- 반복문을 통해 갈 수 있는 그래프의 좌표를 탐색한다

- 현재 탐색하는 좌표가 오른쪽 아래 맨 끝 점이면 반복을 멈추고 오른쪽 아래 맨 끝 점까지 이동 가능한 개수를 출력한다.

- 오른쪽과 아래로 이동할 수 있다면 이동하고 그전 좌표까지 이동 가능한 값을 더한다.

'''
import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1


for i in range(n):
    for j in range(n):

        if i == n - 1 and j == n - 1:
            print(dp[i][j])
            break

        if j + graph[i][j] < n:
            dp[i][j + graph[i][j]] += dp[i][j]

        if i + graph[i][j] < n:
            dp[i + graph[i][j]][j] += dp[i][j]
