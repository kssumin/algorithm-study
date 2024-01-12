import sys
input = sys.stdin.readline

N = input().rstrip()
N_len = len(N)
N_set = set()
for i in range(N_len):
    for j in range(N_len-i):
        N_set.add(N[j:j+i+1])
print(len(N_set))

