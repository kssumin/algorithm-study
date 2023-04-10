'''
문제 : A -> B
난이도 : 실버2

#1
B에서 A로 가보자
'''
import sys

a, b = map(int, sys.stdin.readline().split())

count = 0
while a < b:
    if (b % 2 == 0):
        b = b // 2
        count += 1
    else:
        str_b = str(b)
        if (str_b[-1] == "1"):
            b = int(str_b[:-1])
        else:
            break

        count += 1


if (a == b):
    print(count+1)
else:
    print(-1)
