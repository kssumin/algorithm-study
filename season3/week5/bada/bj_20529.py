'''
문제 : 가장 가까운 세 사람의 심리적 거리
난이도 : 실버1
'''

import sys
from itertools import combinations


def distance(s1, s2, s3):
    count = 0
    for i in range(4):
        if s1[i] != s2[i]:
            count += 1

    for i in range(4):
        if s2[i] != s3[i]:
            count += 1

    for i in range(4):
        if s1[i] != s3[i]:
            count += 1
    return count


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    people = list(sys.stdin.readline().split())
    if n > 32:
        print(0)
    else:
        answer = 100
        comb_list = list(combinations(people, 3))
        for c in comb_list:
            answer = min(answer, distance(c[0], c[1], c[2]))
        print(answer)
