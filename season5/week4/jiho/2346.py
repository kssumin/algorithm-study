from collections import deque
import sys
input = sys.stdin.readline

cnt = int(input()) # balloon count
balloon_lst = deque(enumerate(map(int, input().split()),start=1)) # balloon input

for i in range(cnt):
    p = balloon_lst.popleft() # first balloon pop
    print(p[0], end=" ")
    if p[1] > 0:
        balloon_lst.rotate(-(p[1] - 1))
    else:
        balloon_lst.rotate(-p[1])
