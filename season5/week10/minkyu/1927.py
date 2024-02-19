import sys
import heapq

input = sys.stdin.readline
N = int(input())
num_list = []

for i in range(N):
    num = int(input())
    if num == 0:
        if not num_list:
            print(0)
        else:
            print(num_list[0])
            heapq.heappop(num_list)
    else:
        heapq.heappush(num_list, num)

