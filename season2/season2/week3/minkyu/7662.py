import sys
import heapq
input = sys.stdin.readline


def queue():
    K = int(input().rstrip())
    max_queue = []
    min_queue = []
    visited = [False] * K
    for j in range(K):
        alpha, num = input().rstrip().split()
        num = int(num)
        if alpha == 'I':
            heapq.heappush(max_queue, (-num, j))
            heapq.heappush(min_queue, (num, j))
            visited[j] = True
        elif alpha == 'D':
            if num == 1:
                # max_queue 에 숫자가 존재하고 해당 숫자의 visited 가 false 라면
                while max_queue and not visited[max_queue[0][1]]:
                    heapq.heappop(max_queue)
                if max_queue:
                    visited[max_queue[0][1]] = False
                    heapq.heappop(max_queue)
            else:
                # min_queue 에 숫자가 존재하고 해당 숫자의 visited 가 false 라면
                while min_queue and not visited[min_queue[0][1]]:
                    heapq.heappop(min_queue)
                if min_queue:
                    visited[min_queue[0][1]] = False
                    heapq.heappop(min_queue)

    # visited 가 false 라면 max 에서 삭제된 숫자가 min 에 있거나 min 에서 삭제된 숫자가 max 에 있다는 뜻
    # 따라서 pop 해준다.
    while min_queue and not visited[min_queue[0][1]]:
        heapq.heappop(min_queue)
    while max_queue and not visited[max_queue[0][1]]:
        heapq.heappop(max_queue)

    if not min_queue or not max_queue:
        print("EMPTY")
    else:
        max_num = -max_queue[0][0]
        min_num = min_queue[0][0]
        print(max_num, min_num)


T = int(input())
for i in range(T):
    queue()
"""
처음 한 생각
min_queue 와 max_queue 를 만들어 각각에서 최솟값, 최댓값을 제거한 후 합친 다음 합친 것에서 최댓값과 최솟값을 출력한다.

첫 번째 짠 코드
max_queue 와 min_queue 를 만들어 최댓값은 max 에서, 최솟값은 min 에서 pop 을 해주고 나중에 교집합만 남기고
그 중 최솟값, 최댓값을 출력하려고 했는데 이렇게 하면 pop 한 숫자가 max_queue 나 min_queue 에 남아있게 된다.
그래서 잘못됐다...


def queue():
    K = int(input())
    max_queue = []
    min_queue = []
    cnt = 0
    for i in range(K):
        alpha, num = input().rstrip().split()
        num = int(num)
        if alpha == 'I':
            heapq.heappush(max_queue, -num)
            heapq.heappush(min_queue, num)
            cnt += 1
        elif alpha == 'D' and cnt > 0:
            if num == 1:
                heapq.heappop(max_queue)
            else:
                heapq.heappop(min_queue)
            cnt -= 1

    max_queue = list(map(lambda x: x * -1, max_queue))
    list_queue = set(max_queue) & set(min_queue)

    if list_queue:
        print(max(list_queue), min(list_queue))
    else:
        print("EMPTY")
    return

두 번째 짠 코드
D가 1일 때는 Q에 -1씩 곱해주고 pop 을 해준다. 또 같은 숫자가 들어오면 pop 해주고 1이였다가 -1, 또는 -1이였다가 1로 변하면
또 Q에 -1씩 곱해주고 pop 해준다. 시간초과가 날 거 같았지만 그래도 해봤다. 

def put_minus(lt):
    return list(map(lambda x:x*-1, lt))
    
def queue():
    K = int(input())
    Q = []
    previous = -1
    for i in range(K):
        alpha, num = input().rstrip().split()
        num = int(num)
        if alpha == 'I':
            heapq.heappush(Q, num)
        elif alpha == 'D' and Q:
            if num == 1:
                if previous == 1:
                    heapq.heappop(Q)
                elif previous == -1:
                    Q = put_minus(Q)
                    heapq.heappop(Q)
            elif num == -1:
                if previous == 1:
                    Q = put_minus(Q)
                    heapq.heappop(Q)
                elif previous == -1:
                    heapq.heappop(Q)
    min_num = heapq.heappop(Q)
    if Q:
        max_num = max(Q)
    else:
        max_num = min_num
    print(max_num, min_num)
    return

세 번째 짠 코드
이것도 시간초과가 날 것 같았는데 짜 봤다.
max 함수로 입력 들어온 숫자 중 가장 큰 숫자를 max_num에 저장한다
만약 D 1이 들어온다면 그 숫자를 remove 함수를 이용해서 remove 를 해준다.
그 바로 다음 D 1이 들어온다면 문제가 발생한다. 현재 최댓값을 몰라서 max 함수로 또 구해주어야한다.
max 함수가 시간이 오래 걸려서 시간초과가 난 것 같다.

INF = 1e9

def queue():
    K = int(input())
    Q = []
    max_num = -INF

    for i in range(K):
        alpha, num = input().rstrip().split()
        num = int(num)
        if alpha == 'I':
            max_num = max(num, max_num)
            heapq.heappush(Q, num)
        elif alpha == 'D' and Q:
            if num == 1:
                Q.remove(max_num)
                max_num = max(Q)
            elif num == -1:
                heapq.heappop(Q)
    if Q:
        max_num = max(Q)
        min_num = heapq.heappop(Q)
    else:
        print("EMPTY")
        return
    print(max_num, min_num)
    return


T = int(input())
for i in range(T):
    queue()

네 번째 짠 코드
이것도 시간초과가 날 것 같긴했는데 그냥 짜 봤다.
remove 함수의 시간복잡도가 O(n)인데다가 그 함수를 D를 입력 받을 때마다 해줘야하니
시간 초과가 난 것 같다.
def queue():
    K = int(input().rstrip())
    max_queue = []
    min_queue = []
    for i in range(K):
        alpha, num = input().rstrip().split()
        num = int(num)
        if alpha == 'I':
            heapq.heappush(max_queue, -num)
            heapq.heappush(min_queue, num)
        elif alpha == 'D' and max_queue:
            if num == 1:
                max_num = -heapq.heappop(max_queue)
                min_queue.remove(max_num)
            else:
                min_num = heapq.heappop(min_queue)
                max_queue.remove(-min_num)

    if max_queue:
        if len(max_queue) == 1:
            max_num = -heapq.heappop(max_queue)
            min_num = max_num
        else:
            max_num = -heapq.heappop(max_queue)
            min_num = heapq.heappop(min_queue)
    else:
        print("EMPTY")
        return
    print(max_num, min_num)
    return

풀이
안 풀려서 구글링 해봤다.
처음에 아래 설명과 같이 짜려고 했었는데 저러면 중복값을 처리하지 못해서 저렇게 안 짰는데 저 아이디어와 비슷하게
visit 리스트를 만들면 되는거였다. 안 보고 풀 수 있었는데 아쉽다.
와 근데 제출을 함수만 해서 자꾸 왜 틀린지 모르고 계속 찾고 있었다. 미치는 줄

set에 입력 들어오는 숫자들을 다 저장하고, 최댓값이나 최솟값을 pop할 때는 set에 있는 숫자만 pop으르 한다.
max_queue나 min_queue에서 pop 되면 set에서도 삭제한다. 
"""
