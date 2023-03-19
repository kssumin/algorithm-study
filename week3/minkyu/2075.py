import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
for i in range(N):
    for num in list(map(int, input().split())):
        heapq.heappush(heap, num)
        if len(heap) > N:
            heapq.heappop(heap)

print(heapq.heappop(heap))
"""
첫 번째 코드
난 이 코드가 맘에 든다.
우리가 실제 N*N 표를 봤을 때 N번째 큰 숫자를 어떻게 알아내는지 생각해보고 그거랑 똑같이 구현했다.
처음에는 일단 각 열의 마지막 숫자를 비교한다. 그 5개 중 가장 큰 숫자를 지우고 그 위의 숫자를 추가한다.
또 5개를 비교하고 반복한다. 몇 번 지웠는지 세고 N번째 때에는 지우지 않고 출력한다.
아마 N*N 값을 전부 graph 에 추가해서 메모리 초과가 난 것 같은데 아쉽다...
이 문제를 왜 시간으로 분별하지 않고 메모리로 분별했을까 생각해보면 NlogN값이 너무 작아서 그런가...? 모르겠다.. 슬프다
내 코드는 메모리는 많이 잡아먹어도 시간은 적게 들텐데 ㅠ

N = int(input())
graph = []
heap = []
for i in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    heapq.heappush(heap, (-graph[-1][i], i))
    graph[-1][i] = 0

cnt = 0
while 1:
    cnt += 1
    if cnt == N:
        print(-heapq.heappop(heap)[0])
        break
    index = heapq.heappop(heap)[1]
    tmp = -1
    while 1:
        if graph[tmp][index] == 0:
            tmp -= 1
        else:
            heapq.heappush(heap, (-graph[tmp][index], index))
            graph[tmp][index] = 0
            break

두 번째 코드
그냥 짜 봤다.
heap 에다가 다 뭉텅이로 집어넣고 큰 숫서대로 출력한다.
당연히 메모리 초과가 떴다.
N = int(input())
heap = []
for i in range(N):
    for num in list(map(int, input().split())):
        heapq.heappush(heap, -num)

for i in range(N - 1):
    heapq.heappop(heap)

print(-heapq.heappop(heap))

풀이
어떻게 메모리를 줄일지 모르겠어서 질문 게시판을 참고했다.
heap 에 넣는 거는 똑같은데 heap의 크기가 N개가 넘을 필요는 없으니 넘을 때마다 heappop 을 해버린다.
파이썬은 최소힙으로 구현되어 있기 때문에 heappop을 하면 heap 리스트 중 최소값이 사라진다. 우리가 필요한 값은
N번째로 큰 값이기에 for 문을 다 돌고 나면 heap 에는 들어온 값 중 1~N번째로 큰 값이 들어 있다.
따라서 그 상태에서 바로 heappop 을 하면 N번째로 큰 값이 출력된다.
"""
