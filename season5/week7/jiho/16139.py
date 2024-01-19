import sys; input = sys.stdin.readline

str = input()
N = int(input())
for i in range(N):
    alpha, A, B = input().split()
    a = int(A)
    b = int(B)
    count_alpha = str[a:b+1].count(alpha)
    print(count_alpha)
