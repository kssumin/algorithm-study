import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while 1:
        min_food = heapq.heappop(scoville)
        if min_food >= K:
            break
        if not scoville:
            return -1
        second_food = heapq.heappop(scoville)
        heapq.heappush(scoville, min_food + second_food * 2)
        answer += 1

    return answer

"""
풀이
지호가 힙을 물어봐서 이 문제가 힙을 써야된다는 것을 알아서 쉽게 풀었다.
"""