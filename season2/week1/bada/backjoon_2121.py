'''
2121번 - 넷이 놀기
난이도 - 실버 3
알고리즘 분류 -
'''
import sys

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
points = []
for _ in range(n):
    p = tuple((map(int, sys.stdin.readline().split())))
    points.append(p)

points_set = set(points)
count = 0

for p in points:
    w, h = p
    p1 = (w + a, h)
    p2 = (w, h+b)
    p3 = (w+a, h+b)

    if (p1 in points_set) and (p2 in points_set) and (p3 in points_set):
        count += 1

print(count)