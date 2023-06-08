# 13164 행복 유치원
# https://www.acmicpc.net/problem/13164

N, K = list(map(int, input().split()))
arr = list(map(int, input().split()))

gap = []

for i in range(1, len(arr)):
    gap.append(arr[i] - arr[i-1])

gap.sort()
print(sum(gap[:N-K]))
