# BJ 17626 : Four Squares / SILVER III /

import sys
import math

n = int(sys.stdin.readline().strip())
cnt = 0


def square_sum(n):
    global cnt

    if int(math.sqrt(n)) == math.sqrt(n):
        cnt += 1
        print(cnt)

    else:
        cnt += 1
        if cnt >= 4 and n == 2:
            cnt = 1
            square_sum(n - (int(math.sqrt(n) - 1) ** 2))
        else:
            square_sum(n - (int(math.sqrt(n)) ** 2))



square_sum(n)