import sys
from collections import deque

read = sys.stdin.readline
n = int(read())
li = enumerate([*map(int,read().split())])


q = deque(li)
answer = []

while q:
    cnt = q.popleft()
    r = cnt[1] - 1 if cnt[1] > 0 else cnt[1]
    q.rotate(-r)
    answer.append(cnt[0] + 1)

print(*answer)