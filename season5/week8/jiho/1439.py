# 1, 0 중에 더 많은 거 찾아서 연속 되는 부분 개수만 찾기
# 그냥 바뀌는 부분만 찾으면 될 듯..?

import sys; input = sys.stdin.readline
cnt = 0
N = input()
pre = '?'

for i in N:
    if i != pre:
        pre = i
        cnt += 1

print((cnt - 1) // 2) # 처음에 바뀌는 거 빼주기