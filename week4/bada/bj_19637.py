'''
문제 : IF문 좀 대신 써줘
난이도 : 실버3

'''
import sys

n, m = map(int, sys.stdin.readline().split())

powerList = []
nameList = []

for _ in range(n):
    name, power = sys.stdin.readline().split()
    power = int(power)
    if powerList and powerList[-1] == power:
        continue
    else:
        powerList.append(power)
        nameList.append(name)


for _ in range(m):
    p = int(sys.stdin.readline())
    start, end = 0, len(powerList) - 1
    while start <= end:
        mid = (start + end) // 2
        if (p <= powerList[mid]):
            end = mid - 1
        else:
            start = mid + 1
    print(nameList[end+1])
