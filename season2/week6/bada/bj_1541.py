'''
문제 : 잃어버린 괄호
난이도 : 실버2

괄호가 없는 식을 받으면 괄호를 적절히 쳐서 식의 값을 최소로 만든다

#1
'-' 뒤에 연속되는 '+'들 다 괄호로 묶으면 될 것 같음
'''
import sys

func = str(sys.stdin.readline().strip())


func = func.replace('+', ',+,').replace('-', ',-,')
list_func = func.split(',')

answer = 0
plus = True
for f in list_func:
    if f.isdigit():
        if plus:
            answer += int(f)
        else:
            answer -= int(f)
    else:
        if f == "-":
            plus = False

print(answer)
