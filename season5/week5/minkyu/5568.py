from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
input_list = []
result_set = set()
for _ in range(n):
    input_list.append(int(input()))

if k == 2:
    for a, b in permutations(input_list, 2):
        result_set.add(str(a)+str(b))
elif k == 3:
    for a, b, c in permutations(input_list, 3):
        result_set.add(str(a)+str(b)+str(c))
else:
    for a, b, c, d in permutations(input_list, 4):
        result_set.add(str(a)+str(b)+str(c)+str(d))

print(len(result_set))