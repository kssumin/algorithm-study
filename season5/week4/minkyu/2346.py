import sys
input = sys.stdin.readline

N = int(input())
balloon = list(map(int, input().rstrip().split()))
index = 0
move = balloon[0]
balloon[0] = 0
result = [index + 1]
result_len = 1
while result_len != N:
    while move != 0:
        if move > 0:
            index += 1
        else:
            index -= 1

        if index == N:
            index = 0
        elif index == -1:
            index = N - 1

        if balloon[index] != 0:
            if move > 0:
                move -= 1
            else:
                move += 1
    result.append(index + 1)
    move = balloon[index]
    balloon[index] = 0
    result_len += 1
print(*result, sep=" ")