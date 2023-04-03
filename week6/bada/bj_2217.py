'''
문제 : 로프
난이도 : 실버4

N개의 로프로 들어올릴 수 있는 물체의 최대 중량을 구하자
각 로프가 들어올릴 수 있는 중량은 다르고, 병렬로 연결해서 분산할 수 있다.

#1
병렬해서 들을 수 있는 무게의 최대 + 제외하고 최대 ... + 제외하고 최대 ...
'''
import sys

n = int(sys.stdin.readline())

weights = []
for _ in range(n):
    weights.append(int(input()))
weights.sort()

answer = 0
for i in range(n):
    answer = max(answer, weights[i] * (n - i))

print(answer)
