import sys
import heapq
input = sys.stdin.readline


def get_mid():
    M = int(input())
    count_mid = M // 2 + 1
    print(count_mid)
    mid_list = []
    input_list = []
    result_list = []
    for i in range(M // 10 + 1):
        tmp_list = list(input().rstrip().split())
        for j in range(len(tmp_list)):
            heapq.heappush(input_list, int(tmp_list[j]))
            if j % 2 == 0:
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

풀이만 나중에 써놓을게용
"""