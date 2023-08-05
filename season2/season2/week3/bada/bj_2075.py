'''
문제 : N번째 큰 수 (2075)
난이도 : 실버 2

#1
흠,, 전체를 비교하며 찾으면 너무 비효율적이지 않을까??
최대 힙 이용해서 pop n번 하면 될 것 같은데 메모리 초과가 뜰까봐 걱정된다
-> 메모리 초과,,

#2
최대 힙을 사용해아한다는 생각에 매몰되어서 최소 힙을 사용할 생각을 못 했다!
입력받은 값을 heap에 저장하고 heap의 크기가 n을 넘어가면 heqppop을 한다.
그러면 작은 값들은 사라지고 최종적으로 heap에는 가장 큰 n개의 수만 남겨진다.
그중 가장 작은 값이 우리가 찾고 싶은 N번째 큰 수다.

'''

import sys
import heapq

hq = []
n = int(sys.stdin.readline())

for _ in range(n):
    for i in list(map(int, sys.stdin.readline().split())):
        heapq.heappush(hq, i)
        if len(hq) > n:
            heapq.heappop(hq)

print(heapq.heappop(hq))