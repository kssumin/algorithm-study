from itertools import product


N, M = map(int, input().split())
numbers = [i for i in range(1,N+1)]
p = product(numbers,repeat=M)

for i in p:
    print(*i)

