# BJ 2812 : 크게 만들기 / GOLD III /

import sys

sys.stdin = open("input.txt", "rt")

n, k = list(map(int, sys.stdin.readline().strip().split()))
num = list(sys.stdin.readline().strip())

stack = []

for i in range(n):

    # k가 양수이고, stack이 비어있지 않고, num[i] > stack에 마지막으로 들어간 값일 때 다음을 계속 반복
    while k > 0 and stack and int(num[i]) > stack[-1]:
        # stack[-1]을 제거 : num[i]가 더 크기 때문
        stack.pop()

        # 하나의 값을 제거했으니 k - 1
        k -= 1

    # stack에 num[i]를 더해줌
    stack.append(int(num[i]))

print(''.join(list(map(str, stack[:len(stack)-k]))))


'''
NOTE:
예전에도 못 풀었던 문제인 것 같은데... 또 못 풀었다.. 바보다

'''