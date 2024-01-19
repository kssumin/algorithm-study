import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n_lst = list(map(int, input().split()))
s_lst = [0]
total = 0

for i in range(N):
    total += n_lst[i]
    s_lst.append(total)

for i in range(M):
    a, b = map(int, input().split())
    print(s_lst[b] - s_lst[a - 1])

