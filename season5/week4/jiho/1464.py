from collections import deque
import sys
input = sys.stdin.readline

s = deque(input().rstrip())
mid = []
reverse = []
result = []
for i in s:
    mid.append(ord(i))

current = mid[0]
reverse.append(current)

for i in range(1, len(s)):
    if current < mid[i]:
        reverse.reverse()
        reverse.append(mid[i])
        reverse.reverse()
    else:
        current = mid[i]
        reverse.append(mid[i])

for i in reversed(reverse):
    result.append(chr(i))

str_s = ''.join(result)
print(str_s)
