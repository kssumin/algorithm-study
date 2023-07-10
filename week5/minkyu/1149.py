import sys
input = sys.stdin.readline

N = int(input())
color_list = [[0,0,0]]
rgb_list = [[0,0,0] for _ in range(N + 1)]
dp = [0 for _ in range(N + 1)]

for _ in range(N):
    color_list.append(list(map(int, input().split())))

for i in range(1, N + 1):
    # r, g, b
    rgb_list[i][0] = min(rgb_list[i-1][1], rgb_list[i-1][2]) + color_list[i][0]
    rgb_list[i][1] = min(rgb_list[i-1][2], rgb_list[i-1][0]) + color_list[i][1]
    rgb_list[i][2] = min(rgb_list[i-1][0], rgb_list[i-1][1]) + color_list[i][2]

    dp[i] = min(rgb_list[i][0], rgb_list[i][1], rgb_list[i][2])

print(dp[-1])

"""
처음에 왜 그런진 모르겠는데 dp를 짤 때 dp[i] = dp[i-3] + i-2, i-1, i 번째 합 중 최소라고 하고 풀었다.
점화식을 잘못 짰다. 예제는 통과해서 맞는 줄 알아서 제출했는데 틀렸다.
그래서 아래 링크를 보고 어떻게 푸는지 감을 잡았다.
https://www.acmicpc.net/board/view/101509
"""