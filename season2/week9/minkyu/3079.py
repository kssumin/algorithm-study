import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = []

for i in range(N):
    num_list.append(int(input()))
start, end = 0, (max(num_list) * M) // N

while end >= start:
    mid = (start + end) // 2
    result = 0
    for num in num_list:
        result += mid // num

    if result < M:
        start = mid + 1
    else:
        end = mid - 1

print(start)
"""
처음 문제를 볼 때 어떻게 풀어야하는지 정말 막막했는데 이분탐색이라는 주제와 전에 풀었던 문제를 생각해서 풀어냈다.
출력할 때 start를 출력해야하는지 end를 출력해야하는지 계속 헷갈렸는데 디버그를 하면서 어떤 걸 출력해야하는지 찾아냈다.
이 문제도 전에 풀었던 문제와 유사하게 풀었다.
"""