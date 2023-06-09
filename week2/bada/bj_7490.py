'''
문제 : 0 만들기
난이도 : 골드5

공백은 뭐지

1-2 3-4 5+6 7
1 -23 - 45 + 67

연산자들을 모두 넣고 마지막에 계산해야 한다

연산자를 넣는 것은 백트래킹, 재귀로 구현하고
계산은 eval() 메서드 이용
'''

import sys

t = int(sys.stdin.readline())
oper = [" ", "+", "-"]
answer = []

# 연산자 추가


def addOper(now, ans):
    if now == n+1:
        calc(ans)
        return
    for o in oper:
        addOper(now+1, ans + o + str(now))

# 계산


def calc(ans):
    tmp = ans.replace(' ', '')
    if eval(tmp) == 0:
        answer.append(ans)


for _ in range(t):
    n = int(sys.stdin.readline())
    addOper(2, "1")
    answer.append(" ")

print(*answer, sep="\n")
