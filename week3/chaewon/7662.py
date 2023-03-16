# BJ 7662 : 이중 우선순위 큐 / GOLD IV /

import sys
import heapq

sys.stdin = open("input.txt", "rt")
t = int(sys.stdin.readline().strip())

min_heap = []
max_heap = []


for _ in range(t):
    k = int(sys.stdin.readline().strip())

    for _ in range(k):
        s, n = sys.stdin.readline().strip().split(' ')
        n = int(n)

        if s == 'I':
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)

        if s == 'D':
            if n == 1 and max_heap:
                rm = heapq.heappop(max_heap)
                min_heap.remove(-rm)
            if n == -1 and min_heap:
                rm = heapq.heappop(min_heap)
                max_heap.remove(-rm)


if not min_heap:
    print('EMPTY')
else:
    max_ = heapq.heappop(max_heap) * (-1)
    min_ = heapq.heappop(min_heap)

    print(max_, min_)
