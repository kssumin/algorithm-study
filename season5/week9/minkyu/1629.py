import sys
input = sys.stdin.readline


def solution(A, B, C):
    if B == 1:
        return A % C
    elif B % 2 == 0:
        return (solution(A, B//2, C) ** 2) % C
    else:
        return ((solution(A, B//2, C)**2) * A) % C


A, B, C = map(int, input().split())
print(solution(A,B,C))
