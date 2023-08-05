# BJ 2121 : 넷이 놀기 / SILVER III / 1272ms

import sys

n = int(sys.stdin.readline().strip())

a, b = map(int, sys.stdin.readline().strip().split(' '))

points = list()
for _ in range(n):
    point = tuple(map(int, sys.stdin.readline().strip().split(' ')))
    points.append(point)

points_set = set(points)

cnt = 0

for i in range(n):
    x1, y1 = points[i]

    p2 = (x1 + a, y1)
    p3 = (x1, y1 + b)
    p4 = (x1 + a, y1 + b)

    if (p2 in points_set) and (p3 in points_set) and (p4 in points_set):
        cnt += 1

print(cnt)


'''
NOTE:

python의 set도 해시의 일종이라는 사실을 알았다!!

순간 tuple이랑 헷갈려서 좀 막혔는데 이 기회에 개념을 확실히 익혔당 오예

'''