'''
문제 : 입국심사
난이도 : 골드5
'''
import sys

n, m = map(int, sys.stdin.readline().split())
times = []

for _ in range(n):
    times.append(int(sys.stdin.readline()))

start, end = 1, max(times) * m
answer = end

while start <= end:
    mid = (start + end) // 2

    count = 0
    for t in times:
        count += mid // t

    if count >= m:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
