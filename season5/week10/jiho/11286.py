# x에 뭐를 넣는다
# 입력값이 0이 아니면 힙에 넣고, 입력값이 0이 절댓값이 가장 작은 수 out, 여러 개면 가장 작은 수
import sys; input = sys.stdin.readline
import heapq
from collections import deque

max_heap = [] # 음수 담을 거
min_heap = [] # 양수 담을 거

n = int(input())
for i in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(min_heap, x)
    elif x < 0:
        heapq.heappush(max_heap, -x)
    else:
        if min_heap: # 최소 힙에 원소가 있을 때
            if max_heap: # 최대 힙에도 원소가 있을 때
                if min_heap[0] < max_heap[0]: # 최대 힙의 값이 최소 힙의 값보다 크면
                    print(heapq.heappop(min_heap))
                else:
                    print(-heapq.heappop(max_heap))
            else: # 최소 힙에만 원소가 있을 때
                print(heapq.heappop(min_heap))
        elif max_heap: # 최대 힙에만 원소가 있을 때
            print(-heapq.heappop(max_heap)) # 최대 힙 값은 음수
        else: # 둘 다 없을 때
            print(0)



