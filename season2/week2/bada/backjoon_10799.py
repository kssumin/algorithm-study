'''
문제 : 10799번 쇠막대기
난이도 : 실버2

풀이:
규칙 찾는 게 중요했던 문제

Rule)
1. 레이저가 자를 때 생기는 조각의 개수 = 존재하는 쇠막대기의 개수
2.1. 존재하는 쇠막대기의 개수는 아직 닫히지 않은 "("의 개수
2.2 쇠막대기의 괄호가 닫히면 앞에 존재하는 레이저에 의해 조각이 1개 증가

레이저를 찾기 쉽도록 "()"를 다른 문자로 replace 함
그 후엔 위의 규칙에 따라 조각의 개수를 세어주면 된다.
'''
import sys

input_value = sys.stdin.readline().rstrip()
input_value = input_value.replace("()", "X")

count = 0
answer = 0

for s in input_value:
    if s == "(":
        count += 1
    elif s == ")":
        count -= 1
        answer += 1
    else:
        answer += count

print(answer)