import sys
input = sys.stdin.readline

N = int(input())
num_list = sorted(list(map(int, input().split())))

M = int(input())
result_list = list(map(int, input().split()))
for i in range(len(result_list)):
    start = 0
    end = len(num_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if result_list[i] < num_list[mid]:
            end = mid - 1
        else:
            start = mid + 1
    if result_list[i] == num_list[end]:
        print(1)
    else:
        print(0)