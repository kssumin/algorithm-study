'''
문제 : 1918번 후위표기식
난이도 : 골드2

일단 후위표기식 이름만 들으면 스택을 사용해야 할 것 같다.

후위표기식 규칙
1) 피연산자 : 스택에 넣지않고 그대로 출력
2) 연산자
- 스택이 비어있을 경우 push
- 스택이 비어있지 않은 경우 스택 안의 연산자와 우선순위 비교,
  stack top 연산자가 현재 연산자의 우선순위보다 낮을 때까지 pop & 출력
  현재연산자 push
3) 왼쪽 괄호 '('를 만나면 stack push
4) 오른쪽 괄호 ')'를 만나면 왼쪽 괄호 '('가 나올 때까지 모든 연산자 pop 후 출력 -> '(' 삭제
5) 표기식에 문자가 남지 않았다면 stack을 비움 -> pop & 출력

우선순위
    1. *, /
    2. +, -
    3. ( 
'''
import sys
from collections import deque

# 입력
infix = list(sys.stdin.readline().strip())
postfix = []
stack = deque()
priority = {"*":1, "/":1, "+":2, "-":2, "(":3, ")":3}

for s in infix:
    if s.isalpha():
        postfix.append(s)
    else:
        if len(stack) == 0:
            stack.append(s)
        else:
            if s == "(":
                stack.append(s)
            elif s == ")":
                while stack:
                    top = stack.pop()
                    if top == "(":
                        break
                    else:
                        postfix.append(top)
            else:
                while stack:
                    top = stack.pop()
                    if priority[top] <= priority[s]:
                        postfix.append(top)
                    else:
                        stack.append(top)
                        break
                stack.append(s)

while stack:
    top = stack.pop()
    if top == "(" or top == ")":
        break
    postfix.append(top)

print(''.join(postfix))