import sys
input = sys.stdin.readline

N, M = map(int, input().split())

N_set = set()
M_list = list()
result = []
for i in range(N):
    N_set.add(input().rstrip())
for i in range(M):
    M_list.append(input().rstrip())
for i in range(len(M_list)):
    if M_list[i] in N_set:
        result.append(M_list[i])
result.sort()
print(len(result))

print(*result, sep="\n")