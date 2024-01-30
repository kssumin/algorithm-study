# 기름값이 비싼 데에서 조금 넣고 싼 데에서 많이 넣기
# 처음에는 무조건 넣기
# 기름값이 비싸면 앵꼬나기 전까지, 싸면 끝까지 갈 때 까지 다 넣기
import sys; input = sys.stdin.readline

city = int(input())
distance = list(map(int, input().split()))
oil = list(map(int, input().split()))

minimum = oil[0]
dist = 0

for i in range(city - 1):
    if oil[i] < minimum:
        minimum = oil[i]
    dist += minimum * distance[i]

print(dist)
