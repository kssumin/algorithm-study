import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
ingredient = dict()
for i in range(1, N + 1):
    ingredient[i] = tuple(map(int, input().split()))

result = []
for i in range(1, len(ingredient) + 1):
    tmp = combinations(ingredient.values(), i)
    while 1:
        try:
            element = next(tmp)
            sour = 1
            sweet = 0
            for j in range(i):
                sour *= element[j][0]
                sweet += element[j][1]
                result.append(abs(sour - sweet))
        except:
            break

print(min(result))

"""
저번에 iterable 객체를 배운 기억이 있어서 활용해봤다.
그냥 조합을 써서 모든 경우의 수를 계산했다.
"""