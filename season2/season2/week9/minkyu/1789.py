import sys
input = sys.stdin.readline

S = int(input())
result = 1
for i in range(2, 100000):
    result += i
    if S < result:
        print(i - 1)
        break

"""
오잉 이게 왜 이분탐색이지
"""


