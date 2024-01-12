import sys

input = sys.stdin.readline


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif a < b < c:
        if dp[a][b][c] == 0:
            dp[a][b][c] = w(a, b, c-1) + w(a, b-1 ,c-1) - w(a,b-1,c)
        return dp[a][b][c]
    else:
        if dp[a][b][c] == 0:
            dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return dp[a][b][c]


dp = [[[0 for _ in range(50)] for _ in range(50)] for _ in range(50)]
dp[0][0][0] = 1


while 1:
    a, b, c = list(map(int, input().split()))
    if a == -1 and b == -1 and c == -1:
        break
    print("w({}, {}, {}) = {}".format(a,b,c,w(a,b,c)))