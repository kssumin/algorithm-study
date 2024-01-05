import sys
input = sys.stdin.readline

car_dict = {}
N = int(input())
for i in range(N):
    car_dict[input().rstrip()] = i
car_list = []
for i in range(N):
    car_list.append(input().rstrip())
result = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if car_dict[car_list[i]] > car_dict[car_list[j]]:
            result += 1
            break
print(result)