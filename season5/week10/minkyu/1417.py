import sys
import heapq
input = sys.stdin.readline

N = int(input())
person_list = []

for i in range(N):
    vote_count = int(input())
    if i == 0:
        dasom = vote_count
    else:
        heapq.heappush(person_list, -vote_count)

count = 0
if person_list:
    while -person_list[0] >= dasom:
        count += 1
        heap = heapq.heappop(person_list)
        heap += 1
        dasom += 1
        heapq.heappush(person_list, heap)

print(count)