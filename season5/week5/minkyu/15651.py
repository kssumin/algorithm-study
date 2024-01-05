import sys
input = sys.stdin.readline

def BT():
    if len(result) == M:
        print(*result)
        return
    else:
        for i in range(1, N + 1):
            result.append(i)
            BT()
            result.pop()



N, M = map(int, input().split())
result = []
BT()