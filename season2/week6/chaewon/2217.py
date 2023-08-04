# BJ 2217 : 로프 / SILVER IV / 116ms

import sys

n = int(sys.stdin.readline().strip())
max_w = list(map(int, list(sys.stdin.readline().strip() for _ in range(n)) ))

max_w.sort()

result_list = []

for i in range(n - 1):
    result_list.append(max_w[i] * (n - i))

result_list.append(max_w[-1])

# print(result_list)
print(max(result_list))