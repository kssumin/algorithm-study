'''
문제 : 중앙값 구하기 (2696)
난이도 : 골드 2

#1
난 이렇게 한 줄에서도 여러 개를 입력받고 또 그게 여러 줄 있는 입력이 어렵당,,
-> list extend를 이용하면 된다!!! 하하

nsmallest를 사용하면 안 되는 것 같다. 시간초과
'''
import sys
import heapq

def getMedian(data):
    min_q = []
    max_q = []
    mid = data[0]
    result = [mid]

    for idx, val in enumerate(data[1:]):
        if val > mid:
            heapq.heappush(min_q, val)
        else:
            heapq.heappush(max_q,(-val,val))
        
        if idx % 2 == 1:
            if len(max_q) < len(min_q):
                heapq.heappush(max_q, (-mid,mid))
                mid = heapq.heappop(min_q)
            elif len(max_q) > len(min_q):
                heapq.heappush(min_q,mid)
                mid = heapq.heappop(max_q)[1]
            result.append(mid)

    print(len(result))
    for i in range(len(result)):
        if i != 0 and (i+1) % 10 == 1:
            print()
        print(result[i], end=' ')
    print()



t = int(sys.stdin.readline())

for _ in range(t):
    m = int(input())
    data = []

    if m % 10 == 0:
        for _ in range(m // 10):
            data.extend(list(map(int, sys.stdin.readline().rstrip().split())))
    else:
        for _ in range(m // 10 + 1):
            data.extend(list(map(int, sys.stdin.readline().rstrip().split())))

    getMedian(data)