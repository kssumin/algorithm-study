'''
문제 : 2800번 괄호 제거
난이도 : 골드5


'''
import sys
from itertools import combinations, permutations
import copy

stack = []
temp = []
answer = set()

n = list(sys.stdin.readline().rstrip())

for idx, word in enumerate(n):
    if word == "(":
        stack.append(idx)
    elif word == ")":
        temp.append((stack.pop(), idx))

for i in range(1, len(temp) + 1):
    combi = combinations(temp, i)

    for j in combi:
        copy_n = list(n)

        for k in j:
            copy_n[k[0]] = ""
            copy_n[k[1]] = ""
        answer.add(''.join(copy_n))

for ans in sorted(list(answer)):
    print(ans) 