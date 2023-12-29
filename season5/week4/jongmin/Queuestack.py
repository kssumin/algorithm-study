from collections import deque

N = int(input())

select = list(map(int, input().split()))
numbers = list(map(int,input().split()))
T = int(input())
inputs = list(map(int,input().split()))
qs = deque()
answer = []

for i in range(N-1,-1,-1):
    if select[i] == 0:
        qs.appendleft(numbers[i])

for i in inputs:
    qs.appendleft(i)

for i in range(T):
    answer.append(qs.pop())

print(*answer)