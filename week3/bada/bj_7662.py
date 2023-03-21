'''
문제 : 이중 우선순위 큐 (7662)
난이도 : 골드 4

#1
"I n" 연산과 "D -1" 연산은 push, pop으로 구현
"D 1" 연산은 nsmallest로 구현해보자
-> 시간초과,,,

#2
다른 사람들 코드를 봐봤더니 최대힙 최소힙 2개를 만들어야 한다!
'''
import sys
import heapq


t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    min_heap, max_heap = [], []
    visited = [False] * k
    
    for j in range(k):
        s, n = sys.stdin.readline().split()
        n = int(n)
        if s == "I":
            heapq.heappush(min_heap, (n, j))
            heapq.heappush(max_heap, (-n, j))
            visited[j] = True
        else:
            if n == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            else:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
               
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)


    if len(min_heap) == 0:
        print("EMPTY")
    else:
        print("{} {}".format(-max_heap[0][0], min_heap[0][0]))