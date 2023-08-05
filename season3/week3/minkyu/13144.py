import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

start = 0
end = 0
result = 0
while 1:
    if end == N:
        if start == N - 1:
            result += end - start
            break
        else:
            result += end - start
            end -= 1
            start += 1
    tmp = num_list[start:end+1]
    if num_list[start] == num_list[end] and start != end:
        start += 1
        result += end - start + 1
    else:
        if end - start >= 2 and num_list[end - 1] == num_list[end]:
            start += 1
        end += 1
print(result)

"""
포기
"""