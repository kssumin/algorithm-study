# BJ 7662 : 이중 우선순위 큐 / GOLD IV /

import sys
import heapq

sys.stdin = open("input.txt", "rt")
t = int(sys.stdin.readline().strip())

min_heap = []
max_heap = []


for _ in range(t):
    k = int(sys.stdin.readline().strip())
    visited = [0] * k

    for i in range(k):
        s, n = sys.stdin.readline().strip().split(' ')
        n = int(n)

        if s == 'I':
            # 값을 추가할 때, 해당 값의 아이디인 i를 튜플 형태로 함께 추가
            heapq.heappush(min_heap, (n, i))
            heapq.heappush(max_heap, (-n, i))

            # 추가한 아이디의 visited = 1로 설정
            visited[i] = 1

        if s == 'D':

            # 최댓값을 삭제할 때,
            if n == 1:

                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)

                if max_heap:
                    visited[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)

            elif n == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        print('EMPTY')
    else:
        max_ = - max_heap[0][0]
        min_ = min_heap[0][0]

        print(max_, min_)
