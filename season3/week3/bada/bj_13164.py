'''
문제 : 행복 유치원
난이도 : 골드5

중요한 건 각 학생들간의 키차이...
k 개의 그룹이면 k-1개의 구분선이 필요

원생들간의 키차이가 가장 큰 부분에 구분선 넣기
'''
import sys

n, k = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))

gaps = []
for i in range(n-1):
    gaps.append(heights[i+1] - heights[i])

gaps.sort()
for _ in range(k-1):
    gaps.pop()

print(sum(gaps))
