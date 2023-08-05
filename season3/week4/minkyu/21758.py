import sys
input = sys.stdin.readline

def get_honey(st1, st2, end):
    total_honey = 0
    for start in st1, st2:
        if start < end:
            total_honey += sum(honey[start+1:end+1])
        else:
            total_honey += sum(honey[end:start])
    if st1 < st2 < end:
        total_honey -= honey[st2]
    if end < st1 < st2:
        total_honey -= honey[st1]
    return total_honey

N = int(input())
honey = list(map(int, input().split()))
max_honey = 0
"""
11점 풀이
for st1, st2, end in permutations(range(0,N), 3):
    max_honey = max(max_honey, get_honey(st1, st2, end))
24점 풀이
#벌 꿀 벌
for end in range(1, N - 1):
    max_honey = max(max_honey, get_honey(0, N-1, end))
#벌 벌 꿀
for st1, end in combinations(range(1,N), 2):
    max_honey = max(max_honey, get_honey(0, st1, end))
#꿀 벌 벌
for st1, st2 in combinations(range(1,N), 2):
    max_honey = max(max_honey, get_honey(st1, st2, 0))
55점 풀이
# 벌 꿀 벌
for end in range(1, N-1):
    max_honey = max(max_honey, get_honey(0, N-1, end))
# 벌 벌 꿀
for st2 in range(1, N-1):
    max_honey = max(max_honey, get_honey(0, st2, N-1))
# 꿀 벌 벌
for st1 in range(1, N-1):
    max_honey = max(max_honey, get_honey(st1, N-1, 0))
55점 풀이2
for end in range(1, N-1):
    max_honey = max(max_honey, sum_honey - honey[0] - honey[N-1] + honey[end])
# 벌 벌 꿀
for st2 in range(1, N-1):
    max_honey = max(max_honey, sum_honey - honey[0] - honey[st2] + sum(honey[st2+1:N]))
# 꿀 벌 벌
for st1 in range(1, N-1):
    max_honey = max(max_honey, sum_honey - honey[-1] - honey[st1] + sum(honey[0:st1]))
"""
sum_honey = sum(honey)
# 벌 꿀 벌
for end in range(1, N-1):
    max_honey = max(max_honey, sum_honey - honey[0] - honey[N-1] + honey[end])
# 벌 벌 꿀
for st2 in range(1, N-1):
    max_honey = max(max_honey, sum_honey - honey[0] - honey[st2] + sum(honey[st2+1:N]))
# 꿀 벌 벌
for st1 in range(1, N-1):
    max_honey = max(max_honey, sum_honey - honey[-1] - honey[st1] + sum(honey[0:st1]))
print(max_honey)

"""
순열로 풀었을 때 11점이 나왔다.
그런데 벌꿀벌, 꿀꿀벌, 벌꿀꿀 등과 같이 케이스를 나누어주면 조합으로 바꾸어줄 수 있어 시간을 단축시킬 수 있다.
그래서 24점이 나왔다.
24점 풀이에서는 벌꿀벌의 경우에만 처음과 끝이 정해진 줄 알았는데 나머지에서도 처음과 끝 자리가 정해져있고 가운데만
바꾸어주면 되는 거였다.
그래서 그렇게 풀고 나니 55점이 나왔다.
그런데 계속해서 sum()을 하면서 시간이 오래 걸리는 것 같다.
약간 dp처럼 누적합을 구해놓고 풀이하면 시간이 줄어들것 같다.
"""