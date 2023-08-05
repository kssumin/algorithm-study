import sys
import heapq
input = sys.stdin.readline


def get_mid():
    # 일단 입력값이 몇 개인지 센다.
    M = int(input())
    count_mid = M // 2 + 1
    print(count_mid)
    mid_list = []
    input_list = []
    result_list = []
    # 10개마다 입력을 다시 받는다.
    for i in range(M // 10 + 1):
        # 10개 이하의 입력을 tmp_list 에 저장
        tmp_list = list(input().rstrip().split())
        # input 에 입력받은 숫자를 heappush 해준다.
        for j in range(len(tmp_list)):
            heapq.heappush(input_list, int(tmp_list[j]))
            # j가 0부터 2의 배수일때 홀수개씩 입력됐다는 뜻 
            if j % 2 == 0:
                # mid_list 에 입력값 동기화
                mid_list = input_list[:]
                for k in range(len(input_list)//2):
                    heapq.heappop(mid_list)
                result_list.append(mid_list[0])

    for i in range(count_mid):
        if i == 0:
            pass
        elif i % 10 == 0:
            print()
        print(result_list[i], end=" ")


T = int(input())
for i in range(T):
    get_mid()

"""
처음 짠 코드
1 2 3 4 5 되게 하려고 짠 코드...
5 4 3 2 1 은 안된다.
입력되는 숫자가 점점 줄어들면 안되는 코드
def get_mid():
    M = int(input())
    count_mid = M // 2 + 1
    mid_list = []
    print(count_mid)
    for i in range(M // 10 + 1):
        tmp_list = list(input().rstrip().split())
        if i == 0:
            print(tmp_list[0], end=' ')
        for j in range(1, len(tmp_list)):
            if j % 2 != 0:
                heapq.heappush(mid_list, tmp_list[j])
            else:
                heapq.heappush(mid_list, tmp_list[j])
                print(heapq.heappop(mid_list), end=" ")

16번째 줄에 입력받은 값을 int로 형변환을 안해주고 실행해서 계속 답이 이상하게 나왔다.
저번엔 int() 안해야될걸 했는데 이번엔 해야할걸 안해서 문제가 생겼다...

풀이
숫자를 1개, 3개, 5개 ... 홀수개씩 받을 때마다 mid_list 에 input_list를, 즉 입력받은 값을 계속 동기화해준다.
그리고 숫자가 
1개일때 0개 pop, mid_list[0] 출력,
3개일때 1개 pop, mid_list[0] 출력,
5개일때 2개 pop, mid_list[0] 출력해야 하니 25,26번째줄로 그 작업을 해준다.
그리고 mid_list[0]을 result에 저장해준다.

나중에 29~34줄 코드로 10개씩 출력해준다.
"""
