import sys
from collections import deque
input = sys.stdin.readline

cnt = int(input())
A = list(map(int, input().split())) # queue = 0, stack = 1
B = list(map(int, input().split())) # data structure
M = int(input()) # sequence length
C = list(map(int, input().split()))

queue = deque([])
for i in range(cnt):
    if A[i] == 0:
        queue.appendleft(B[i])
    else:
        if queue == []:
            print(*C)
            break
for i in range(M):
    queue.append(C[i])
    print(queue.popleft(), end= " ")


