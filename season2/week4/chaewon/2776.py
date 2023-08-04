# BJ 2776 : 암기왕 / SILVER IV / 1488ms

import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):

    n = int(sys.stdin.readline().strip())
    note_1 = list(map(int, list(sys.stdin.readline().strip().split())))
    dict1 = dict.fromkeys(note_1, 0)

    m = int(sys.stdin.readline().strip())
    note_2 = list(map(int, list(sys.stdin.readline().strip().split())))

    result = [0] * m

    for i in range(m):
        if note_2[i] in dict1:
            result[i] = 1

    print('\n'.join(map(str, result)))


'''
NOTE:
만약 입력값이 다음과 같다면

n = 5
note_1 = [4, 1, 5, 2, 3]
m = 6
[1, 3, 7, 9, 5, 1]

출력이 수첩2 기준이니까 6줄로 출력되어야 한다!!
즉 [1, 1, 0, 0, 1, 1] 이 출력되어야 함

근데 dict2를 만들어서 계속 중복제거한 값을 가지고 출력하려고 해서 오답 처리 됐다ㅠㅠ


흑 문제 짜증나요! 아래 조건 추가 요청 해놨어요

동규가 같은 질문을 할 수 있다는 조건, 즉, "수첩2에 같은 값이 중복으로 존재할 수 있다"는 조건을 추가해주세요.

'''