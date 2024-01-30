import sys
from itertools import permutations
input = sys.stdin.readline

N = sorted(list(map(int, list(input().rstrip()))), reverse=True)
result = ''
if (0 not in N) or sum(N) % 3 != 0:
    print(-1)
else:
    for perm in permutations(N):
        result = ''
        for num in perm:
            result += str(num)
        result = int(result)
        if result % 30 == 0:
            print(result)
            exit(0)