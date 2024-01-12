import sys
input = sys.stdin.readline

letter = list(input().rstrip())
length = len(letter)
result = length * 2 - 1
for i in range(length - 1, length//2 - 1, -1):
    tmp = length - i - 1
    if letter[i-tmp:i] == letter[length-1:i:-1]:
        result = length + length - tmp * 2 - 1
    if letter[i-tmp-1:i] == letter[length-1:i-1:-1]:
        result = length + length - (tmp + 1) * 2

if result == 0:
    print(1)
else:
    print(result)