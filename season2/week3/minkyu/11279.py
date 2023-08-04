import sys
import heapq
input = sys.stdin.readline

heap = []

N = int(input())

for i in range(N):
    X = int(input())
    if X == 0:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -X)

"""
풀이
저번에 힙을 공부하면서 파이썬에서는 heapq 모듈이 최소 힙으로 되어 있으니 최대 힙으로 바꾸려면 -부호를 붙이면 된다해서 그렇게 풀었다.
"""