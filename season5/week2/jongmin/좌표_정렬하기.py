# 2차원 평면 위의 점 N개
# 1. x좌표 기준
# 2. y좌표 기준 오름차순

N = int(input())
cor = []

for _ in range(N):
    cor.append(tuple(map(int,input().split())))

cor.sort(key=lambda x: (x[0],x[1]))

for x,y in cor:
    print(x,y)