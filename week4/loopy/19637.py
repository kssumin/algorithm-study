# [19637번](https://www.acmicpc.net/problem/19637) IF문 좀 대신 써줘 (실버3)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
titles = []
for i in range(N): 
  T, P = input().split()
  titles.append([T, int(P)])

titles.sort(key=lambda x: x[1])

def binary_search(titles, input_num):
  start = 0
  end = len(titles) - 1
  while start < end:
    mid = (start + end) // 2
    if titles[mid][1] >= input_num:
      end = mid
    else:
      start = mid + 1
  return titles[end][0]

for i in range(M):
  input_num = int(input())
  print(binary_search(titles, input_num))