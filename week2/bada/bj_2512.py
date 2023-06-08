'''
문제 : 예산
난이도 : 실버3

n_list 다 더한 값이 m보다 작으면 n_list 최댓값 출력

m보다 크면???

이분탐색!!!!
'''
import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

if sum(n_list) <= m:
    print(max(n_list))
else:
    # 이분 탐색
    start = 0
    end = max(n_list)
    answer = 0

    while (start <= end):
        mid = (start + end) // 2
        tmp = 0

        for num in n_list:
            if num <= mid:
                tmp += num
            else:
                tmp += mid

        if tmp <= m:
            answer = mid
            start = mid + 1

        else:
            end = mid - 1
    print(answer)
