# 13144 List of Unique Numbers
# https://www.acmicpc.net/problem/13144
# N^2

N = int(input())
arr = list(map(int, input().split()))

def makeValue(arr, i):
    returnValue = set()
    for a in range(len(arr) - i + 1):
        sumValue = 0
        for j in range(i):
            sumValue += (10 ** j) * arr[a + j]
        returnValue.add(sumValue)
    return returnValue

count = 0
for i in range(N):
    count += len(makeValue(arr, i + 1))

print(count)