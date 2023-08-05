'''
문제 : 한국이 그리울 땐 서버에 접속하지
난이도 : 실버3

패턴 a*d -> 시작 글자 a, 마지막 글자 d
'''
import sys
n = int(sys.stdin.readline())
start, end = sys.stdin.readline().strip().split("*")
names = []

for _ in range(n):
    names.append(sys.stdin.readline().strip())

for name in names:
    if len(name) < len(start) + len(end):
        print("NE")
    elif name[:len(start)] == start and name[-len(end):] == end:
        print("DA")
    else:
        print("NE")
