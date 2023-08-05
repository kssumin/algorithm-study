# BJ 2075 : N번째 큰 수 / SILVER II / 1764ms

import sys, heapq

n = int(sys.stdin.readline().strip())

sys.stdin = open("input.txt", "rt")

heap = []

for _ in range(n):

    # 입력받은 n개의 수를 nums에 저장
    nums = list(map(int, list(sys.stdin.readline().strip().split(' '))))

    for i in range(n):
        # 그 n개의 수를 바로 heap에 push
        heapq.heappush(heap, nums[i])

        # heap의 길이가 n보다 커지면 가장 작은 원소를 pop하여, heap의 길이를 n으로 유지
        if len(heap) > n:
            heapq.heappop(heap)


# 최종적으로 heap에는 n개의 원소만 남음
# 이때 heappop 하면 가장 작은 원소, 즉 전체 입력값에서 n번째로 큰 원소가 나옴
k = heapq.heappop(heap)

print(k)


'''
NOTE:

시도 1) graph에 모든 값을 입력 받고, graph의 모든 값을 heap에 넣는 방식
        
        graph = []
        for _ in range(n):
            graph += list(map(int, list(sys.stdin.readline().strip().split(' '))))

        heap = []
        for i in range(n * n):
            heapq.heappush(heap, -graph[i])
        
문제점 : 메모리 초과
N이 최대 1500이라서, 위 코드처럼 하면 최악의 경우 graph에서도 1500*1500개의 요소를, heap에서도 1500*1500의 요소를 모두 저장하게 된다.

--------------------------------------------------------------------
시도 2) 질문 게시판을 확인해보니, 만약 heap의 길이가 n이 넘으면 바로바로 pop을 진행해서 heap의 길이가 n으로 유지되게끔 하면 된다고 했다.

        가장 큰 N개의 수만 가지고 있으면 됩니다.
        heap에 넣으면서 크기가 N보다 크면 가장 작은 것 하나 버리는 것을 반복하면 
        끝날 때는 N개가 남을 것이고 그 중 가장 작은 것을 출력하면 되겠죠?

graph와 heap 둘 중 하나만 사용해도 될 것 같다는 생각이 들었는데,

어떻게 입력받은 값을 요소 하나하나로 분리하여 heap에 넣을 수 있을지,
그리고 heappush를 하면서 동시에 heap의 길이 검사와 pop 수행을 어떻게 구현해야 하는지 고민했다.

중간에 여러 시행착오를 거쳐서 정답 코드를 제출했다!

heapq 모듈 사용에 대해 잘못알고 있던 부분이 있어서 조금 헷갈렸다ㅠ

heapq.heappop(heap)은 무조건 가장 작은 원소를 삭제 및 반환하는 건데
루트 노드의 값을 삭제 및 반환하는 거라고 착각했다.

관련 내용은 발표 자료로 준비해보겠어요!

'''