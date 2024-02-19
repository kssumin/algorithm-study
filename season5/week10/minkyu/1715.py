import sys
import heapq
input = sys.stdin.readline
result = 0

N = int(input())
heap = []
for _ in range(N):
    heapq.heappush(heap, int(input()))
if N == 1:
    print(0)
    exit(0)

while heap:
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    tmp = num1 + num2
    heapq.heappush(heap, tmp)
    result += tmp

    if len(heap) == 1:
        print(result)
        break


