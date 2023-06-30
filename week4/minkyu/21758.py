from itertools import permutations
import sys
input = sys.stdin.readline

def get_honey(st1, st2, end):
    total_honey = 0
    for start in st1, st2:
        if start < end:
            total_honey += sum(honey[start+1:end+1])
        else:
            total_honey += sum(honey[end:start])
    if st1 < st2 < end or end < st2 < st1:
        total_honey -= honey[st2]
    if st2 < st1 < end or end < st1 < st2:
        total_honey -= honey[st1]
    return total_honey

N = int(input())
honey = list(map(int, input().split()))
max_honey = 0
for st1, st2, end in permutations(range(0,N), 3):
    max_honey = max(max_honey, get_honey(st1, st2, end))
print(max_honey)

"""
이렇게 풀면 부분점수일 거 같았는데 역시 부분점수 받았당....
일단 담 문제 풀고 와야겠다
"""