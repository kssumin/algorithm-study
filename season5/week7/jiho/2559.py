import sys
input = sys.stdin.readline

N, K = map(int, input().split())
n_lst = list(map(int, input().split()))

part_sum = sum(n_lst[:K])
s_lst = [part_sum]

for i in range(0, len(n_lst) - K):
    part_sum = part_sum - n_lst[i] + n_lst[i+K]
    s_lst.append(part_sum)

print(max(s_lst))
