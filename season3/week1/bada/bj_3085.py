'''
문제 : 사탕 게임
난이도 : 실버 2

nxn 크기에 사탕
사탕의 색이 다른 인접한 두 칸을 고르고 서로 교환
모두 같은 색으로 이루어져 있는 가장 긴 연속 부분을 고른 다름 그 사탕을 모두 먹음
먹을 수 있는 사탕의 최대 개수?

교환은 한 번만 이루어짐

힌트: n이 굉장히 작다!

교체하고 길이 확인
'''
import sys

n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline()) for _ in range(n)]
answer = 0


def check(arr):
    n = len(arr)
    answer = 1

    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
                answer = max(cnt, answer)
            else:
                cnt = 1

        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
                answer = max(answer, cnt)
            else:
                cnt = 1

    return answer


for i in range(n):
    for j in range(n):
        # 열 바꾸기
        if j+1 < n:
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
            tmp = check(graph)
            answer = max(answer, tmp)
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]

        # 행 바꾸기
        if i+1 < n:
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]
            tmp = check(graph)
            answer = max(answer, tmp)
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]

print(answer)
