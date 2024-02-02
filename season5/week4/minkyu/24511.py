import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
queue_list = []
for i in range(len(A)):
    if A[i] == 0:
        queue_list.append(i)

B = list(map(int, input().split()))
M = int(input())
C = deque((map(int, input().split())))
result = []
while C:
    q = C.popleft()
    for i in queue_list:
        q, B[i] = B[i], q
    print(q,end=" ")
