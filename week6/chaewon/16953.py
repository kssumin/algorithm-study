# BJ 16953 : A → B / SILVER II / 40ms

import sys
# sys.stdin = open("input.txt", "rt")

a, b = map(int, sys.stdin.readline().strip().split())
odds = ['3', '5', '7', '9']
cnt = 1


def solution(a, b):
    global cnt
    if b % 2 == 0 and len(str(b)) > 0:
        b = b // 2

        if a == b:
            cnt += 1
            return 0
        else:
            cnt += 1
            solution(a, b)

    elif str(b)[-1] in odds:
        cnt = -1
        return 0

    elif len(str(b)) > 0:
        b = str(b)
        b = int(b[:-1])

        if a < b:
            cnt += 1
            solution(a, b)
        elif a == b:
            cnt += 1
            return 0
        else:
            cnt = -1
            return 0


solution(a, b)

print(cnt)


'''
NOTE:
처음에는 23~25줄의 조건문을 작성하지 않아서 오답처리되었다.
원인 파악을 못하고 있었는데,
바다가 b의 일의 자리가 3, 5, 7, 9일 때는 -1을 반환해야 한다고 알려줬다!!

조건에 따라 a→b가 가능하게 하려면,
b는 2의 배수이거나, 일의 자리가 1일 수밖에 없다.

그래서 조건문을 추가해서, 일의 자리가 1이 아닌 홀수일 때 -1을 출력하도록 했다.

'''