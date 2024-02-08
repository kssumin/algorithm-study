import sys; input = sys.stdin.readline

A = int(input())
A_lst = set(input().split())
B = int(input())
B_lst = input().split()

for i in B_lst:
    if i in A_lst:
        print(1)
    else:
        print(0)