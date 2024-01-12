import sys

N = int(input())
num_lst = map(int, sys.stdin.readline().rstrip().split())
num_lst = list(num_lst)

rank = 0
min_num = min(num_lst)
rank_lst = {}

for i in sorted(num_lst):
    if i > min_num:
        min_num = i
        rank += 1
    rank_lst[i] = rank

for i in range(len(num_lst)):
    print(rank_lst[num_lst[i]], end=" ")
