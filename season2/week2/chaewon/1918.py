# BJ 1918 : 후위 표기식 / GOLD II / 40ms

infix_not = list(input())
stack = []
result = ''

for s in infix_not:

    # alphabet이면
    if s.isalpha():
        # result에 더해줌
        result += s

    # alphabet이 아니면 = 연산자 또는 괄호
    else:

        # 여는 괄호면 그것을 스택에 넣음
        if s == '(':
            stack.append(s)

        # 곱셈이나 나눗셈이면
        elif s == '*' or s == '/':

            # 스택이 비어있지 않고, 스택의 최상단이 곰셈이나 연산자라면
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                # result에 stack.pop을 계속 추가
                result += stack.pop()
            # stack에 연산자 삽입
            stack.append(s)

        # 덧셈이나 뺄셈이면
        elif s == '+' or s == '-':

            # 스택이 비어있지 않고, 스택의 최상단이 여는 괄호가 아니라면
            while stack and stack[-1] != '(':
                # result에 stack.pop을 계속 추가
                result += stack.pop()
                # stack에 연산자 삽입
            stack.append(s)

        # 닫는 괄호면
        elif s == ')':

            # 스택이 비어있지 않고, 스택의 최상단이 여는 괄호가 아니라면
            while stack and stack[-1] != '(':
                # result에 stack.pop을 계속 추가
                result += stack.pop()
                # stack에 연산자 삽입
            stack.append(s)


# 스택이 빌 때까지 result에 stack.pop 추가
while stack:
    result += stack.pop()

print(result)


'''
NOTE:
예시로 설명하는 게 이해가 더 쉬울 듯함!
로직을 어케 생각해내는지... 참 대단해욧

ex) input = A*(B+C)

infix_not = ['A', '*', '(', 'B', '+', 'C', ')']

for문

1) s = 'A'
    result = 'A'
    stack = []

2) s = '*'
    result = 'A'
    stack = ['*']
    
3) s = '('
    result = 'A'
    stack = ['*', '(']
    
4) s = 'B'
    result = 'AB'
    stack = ['*', '(']

5) s = '+'
    result = 'AB'
    stack = ['*', '(', '+']

6) s = 'C'
    result = 'ABC'
    stack = ['*', '(', '+']
    
7) s = ')'
    result = 'ABC'
    ->  result = 'ABC+'
        stack = ['*', '(']
    ->  result = 'ABC+'
        stack = ['*']
    
while문
    result = 'ABC+*'
    stack = []


'''