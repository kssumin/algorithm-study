import sys
input = sys.stdin.readline


N = int(input())
num_list = list(map(int, input().split()))
result_list = [{} for _ in range(N - 1)]
result_list[0][num_list[0]] = 1
cnt = 0
for i in range(N - 2):
    for num in result_list[i]:
        if 0 <= num + num_list[i + 1] <= 20:
            if i != N - 2:
                if num_list[i + 1] == 0:
                    result_list[i + 1][num + num_list[i + 1]] = result_list[i][num + num_list[i + 1]] * 2
                elif num + num_list[i + 1] not in result_list[i + 1]:
                    result_list[i + 1].setdefault(num + num_list[i + 1], result_list[i][num])
                else:
                    result_list[i + 1][num + num_list[i + 1]] += result_list[i][num]
            else:
                if num + num_list[-2] == num_list[-1]:
                    cnt += result_list[-1][num]

        if 0 <= num - num_list[i + 1] <= 20:
            if i != N - 2:
                if num_list[i + 1] == 0:
                    result_list[i + 1][num - num_list[i + 1]] = result_list[i][num - num_list[i + 1]] * 2
                elif num - num_list[i + 1] not in result_list[i + 1]:
                    result_list[i + 1].setdefault(num - num_list[i + 1], result_list[i][num])
                else:
                    result_list[i + 1][num - num_list[i + 1]] += result_list[i][num]
            else:
                if num - num_list[-2] == num_list[-1]:
                    cnt += result_list[-1][num]

if num_list[-1] in result_list[-1]:
    print(result_list[-1][num_list[-1]])
else:
    print(0)

"""
흠... 나는 간단하게 풀 수 있는 걸 되게 복잡하게 푸는 것 같다.
dp문제가 어려워서 자꾸 생각을 못해내는 것 같다. 어떻게든 풀어내긴 했지만 몇 줄이면 될 코드를 이렇게 풀어서 속상하다...
시간도 상당히 많이 걸렸다.

풀이
리스트에 딕셔너리를 저장한다.
리스트 i + 1번째 딕셔너리에 i번째 딕셔너리 숫자들에서 num_list i번째 있는 숫자를 빼거나 더한 결과를 저장한다. 
"""
