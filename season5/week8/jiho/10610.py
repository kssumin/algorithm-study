import sys; input = sys.stdin.readline
N = int(input())
N_lst = list(map(int, str(N)))
N_lst.sort(reverse=True)
result = int(''.join(map(str, N_lst)))

if result % 30 == 0:
    print(result)
else:
    print(-1)