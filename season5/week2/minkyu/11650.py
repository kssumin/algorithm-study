import sys
input = sys.stdin.readline

N = int(input())
num_list = []
for _ in range(N):
    num_list.append(list(map(int, input().split())))
num_list.sort(key=lambda x: [x[0], x[1]])
for i in range(N):
    print(*num_list[i])