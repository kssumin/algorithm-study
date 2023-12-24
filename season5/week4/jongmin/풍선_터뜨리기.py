# 2346번 풍선 터뜨리기
from collections import deque as dq

N = int(input())

balloon = dq(list(map(int, input().split())))
index = dq([i for i in range(1,N+1)])
pop = []
pointer = 0

for i in range(N):
    print(index)
    pop.append(index.popleft())
    pointer = balloon.popleft()
    pointer = pointer if pointer < 0 else pointer-1
    balloon.rotate(-pointer)
    index.rotate(-pointer)

print(*pop)