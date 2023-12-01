import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
count_dict = {}

tmp_list = sorted(set(num_list))
for i in range(len(tmp_list)):
    count_dict[tmp_list[i]] = i
for i in range(N):
    print(count_dict[num_list[i]], end=" ")
