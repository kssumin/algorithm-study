# 13144 List of Unique Numbers
# https://www.acmicpc.net/problem/13144
N = int(input())
arr = list(map(int, input().split()))

p1 = 0
p2 = 0

count = 0

is_passed = [False for _ in range(100001)]

while(p1 != N and p2 != N):
    if not is_passed[arr[p2]]:
        is_passed[arr[p2]] = True
        p2 += 1
        count += p2 - p1
    else:
        is_passed[arr[p1]] = False
        p1 += 1

print(count)