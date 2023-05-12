'''
문제 : 랜선 자르기
난이도 : 실버2


'''
import sys

k, n = map(int, sys.stdin.readline().split())
lan = []

for i in range(k):
    lan.append(int(sys.stdin.readline()))

start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2
    count = 0

    for l in lan:
        count += l // mid

    if count >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)
