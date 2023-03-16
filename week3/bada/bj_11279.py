'''
문제 : 최대 힙 (11279)
난이도 : 실버 2

#1
heapq의 push, pop을 이용하면 쉽게 구할 수 있을 것 같다
최대 힙으로 풀어야하기 때문에 부호를 변경해서 최대 힙을 구현한다.
'''

import sys
import heapq

hq = []

n = int(sys.stdin.readline())
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(hq) > 0:
            print(-heapq.heappop(hq)) # 최대힙 부호 반대
        else:
            print(0)
    else:
        heapq.heappush(hq, -x) # 최대 힙 부호 반대