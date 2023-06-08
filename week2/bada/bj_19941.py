'''
문제 : 햄버거 분배
난이도 : 실버3

식탁 길이, 햄버거를 선택할 수 있는 거리 -> 햄버거를 먹을 수 있는 사람의 최대 수
'''
import sys

n, k = map(int, sys.stdin.readline().split())
info = list(sys.stdin.readline().strip())

answer = 0

for i in range(n):
    if info[i] == "P":
        start = max(0, i - k)
        end = min(n, i + k + 1)

        if ("H" in info[start:end]):
            idx = info.index("H", start, end)
            info[idx] = "X"
            answer += 1

print(answer)
