# BJ 10799 : 쇠막대기 / SILVER II / 64ms

import sys

bracket = list(sys.stdin.readline().strip())
cnt = 0
stack = []

for i in range(len(bracket)):
    if bracket[i] == '(':
        stack.append('(')

    else:
        if bracket[i-1] == '(':
            stack.pop()
            cnt += len(stack)

        else:
            stack.pop()
            cnt += 1

print(cnt)



'''
NOTE:

1. bracket[i] = '('이면 stack에 넣는다

2. bracket[i] = ')'이면
    1) bracket[i-1] = '('이면, 이 괄호 쌍은 레이저를 의미 
        - 그러므로 stack에 들어있는 bracket[i-1] = '('을 pop
        - 그리고 stack의 길이를 cnt에 더해줌
          stack에 들어있는 '(' 개수만큼의 파이프가 모두 이 레이저에 의해 잘림
          즉 절단 후 생성된 조각 = '('의 개수 = stack의 길이
    
    2) bracket[i-1] = ')'이면, 이 괄호는 파이프의 끝을 의미
        - 이 경우 stack[-1] = '('인데 이것을 pop함
        - cnt에 1을 더해줌
          이 파이프 괄호 속의 레이저에 의해 파이프는 절단되었을 것인데,
          절단되어 생긴 왼쪽 조각은 이미 1)에서 더해줌
          절단되어 생긴 가장 오른쪽 조각은 항상 1개이기 때문에 1을 더해준다!!

--------------------------------------------------
구글링해서 원리를 이해해봤다.
사실 보고도 cnt에 stack의 길이를 더해준다거나 1을 더해주는 것이 이해가 안돼서
직접 펜으로 적어보면서 개수를 세어봤다.
어려워!! 흑흑
'''