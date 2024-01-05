import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
k = int(input())
lst = [input().rstrip() for _ in range(n)]
lst_set = set()

for i in permutations(lst, k):
    lst_set.add(''.join(i))
print(len(lst_set))
