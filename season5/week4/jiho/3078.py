from collections import deque
import sys
input = sys.stdin.readline

name_lst = deque()
cnt = 0

N, K = map(int, input().split())
for i in range(N):
    name = input().rstrip()
    name_lst.append((name, i + 1))

for name, i in enumerate(name_lst):  # 이름의 길이가 K와 같을 때,
    for name2, j in enumerate(name_lst):
        if i != j and len(name) == len(name2) and abs(i - j) <= 2:
            cnt += 1

print(cnt)