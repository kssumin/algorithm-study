import sys
from itertools import product
input = sys.stdin.readline

n, r = map(int, input().split())
lst = []
for i in range(1, n+1):
    lst.append(i)

for i in product(lst, repeat=r):
    for num in i:
        print(num, end=' ')
    print()
