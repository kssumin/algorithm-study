'''
문제 : 센서
난이도 : 골드5

#1
모르겠다!!!!!!
각 집중국 간의 거리를 일단 구해볼까? -> dist
k개 묶음을 만드려면 k-1개를 지워야함
dist에서 큰 값 k-1개 지우고 합하면 정답

'''
import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

p = list(map(int, sys.stdin.readline().split()))
p.sort()

dist = []
for i in range(n-1):
    dist.append(p[i+1] - p[i])
dist.sort()
print(sum(dist[:n-k]))
