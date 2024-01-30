# 삽입한 다음 작은 수로 넣은 다음
# 두 수 합한 거 고대로 앞에다 넣은 다음
# 계속 반복
import sys; input = sys.stdin.readline
import heapq

cnt = int(input())
cards = []
compare = 0
for i in range(cnt):
    heapq.heappush(cards, int(input()))

while len(cards) > 1:
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    sum_value = card1 + card2

    compare += sum_value
    heapq.heappush(cards, sum_value)

print(compare)