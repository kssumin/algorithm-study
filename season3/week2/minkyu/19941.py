import sys
input = sys.stdin.readline


def check(index):
    global cnt
    if 0 <= index -  K:
        start = index - K
    else:
        start = 0
    if index + K <= N - 1:
        end = index + K
    else:
        end = N - 1
    for i in range(start, end + 1):
        if graph[i] == 'H':
            graph[i] = 'X'
            cnt += 1
            break

N, K = map(int, input().split())
graph = list(input().rstrip())
cnt = 0
for i in range(len(graph)):
    if graph[i] == 'P':
        check(i)
print(cnt)

"""
풀이
그리디로 풀었다
왼쪽에 멀리 있는 햄버거부터 먹게 했다. 
"""