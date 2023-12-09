import sys

a = set()
b = []
c = []
cnt = 0
N, M = map(int, sys.stdin.readline().split())
for i in range(N):
    x = sys.stdin.readline().rstrip()
    a.add(x)
for j in range(M):
    y = sys.stdin.readline().rstrip()
    b.append(y)

for i in range(M):
    if b[i] in a:
        cnt += 1
        c.append(b[i])
print(cnt)
c.sort()
print(*c, sep="\n")

