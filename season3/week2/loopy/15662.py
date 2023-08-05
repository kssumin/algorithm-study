# 15662 톰니바퀴(2) // solve
# https://www.acmicpc.net/problem/15662
N = int(input())
saws = [list(map(int, list(input()))) for _ in range(N)]
M = int(input())
moves = [list(map(int, input().split())) for _ in range(M)]

def moveSawLeft(arr): 
    rArr = arr[1:]
    rArr.append(arr[0])
    return rArr

def moveSawRight(arr):
    rArr = arr[:-1]
    rArr.insert(0, arr[-1])
    return rArr

def toggle(N):
    return 1 if N == -1 else -1

for move in moves:
    [T, mo] = move
    prevMo = mo
    beforemoved = saws[:]

    if mo == 1:
        mo = -1
        beforemoved[T-1] = moveSawRight(saws[T-1])
    else:
        mo = 1
        beforemoved[T-1] = moveSawLeft(saws[T-1])

    mo = prevMo

    for i in range(T-1, 0, -1): # 좌측비교
        if saws[i][6] != saws[i-1][2]:
            mo = toggle(mo)
            if mo == 1:
                beforemoved[i-1] = moveSawRight(saws[i-1])
            else:
                beforemoved[i-1] = moveSawLeft(saws[i-1])
        else:
            break

    mo = prevMo

    for i in range(T, N): # 우측 비교 
        if saws[i][6] != saws[i-1][2]:
            mo = toggle(mo)
            if mo == 1:
                beforemoved[i] = moveSawRight(saws[i])
            else:
                beforemoved[i] = moveSawLeft(saws[i])
        else:
            break

    saws = beforemoved

count = 0
for i in saws:
    if i[0] == 1:
      count += 1

print(count)