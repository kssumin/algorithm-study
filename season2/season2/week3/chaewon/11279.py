# BJ 11279 : 최대 힙 / SILVER II / 136ms

import heapq
import sys

n = int(sys.stdin.readline().strip())

arr = list(map(int, list(sys.stdin.readline().strip() for _ in range(n))))

heap = []

for i in range(n):
    if arr[i] > 0 :
        heapq.heappush(heap, -arr[i])
        
    elif arr[i] == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
 
 
            
'''
NOTE:

heapq 모듈은 최대 힙을 제공하지 않아서,
위 코드처럼 힙에 값을 push할 때 값의 부호를 변경하여 최소 힙으로 정렬 후
출력 시 다시 부호를 바꾸어주어 최대 힙의 결과를 얻을 수 있었다

이 부분은 heapq로 최대 힙 구현하는 방법을 구글링해서 알아냈다!

'''