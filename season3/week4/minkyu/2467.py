import sys
input = sys.stdin.readline

N = int(input())

water = list(map(int, input().split()))
left, right = 0, N-1

INF = sys.maxsize
result = []

while left < right:
    sum1 = water[left] + water[right]
    if abs(sum1) < INF:
        INF = abs(sum1)
        result = [water[left], water[right]]
    if sum1 < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])

"""
옛날에 투포인터로 푼 기억이 났다.
어렴풋이 옛날 풀이가 기억이 났는데 이번 문제는 투포인터로 안 풀릴 것 같아서 이분탐색으로 풀어봤다.
근데 그것도 잘못 풀었다.
그래서 그냥 투 포인터로 풀었다. 옛날에는 풀었던 문제를 못 풀어서 조금 슬프다.
"""