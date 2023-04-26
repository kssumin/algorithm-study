# BJ 2047 : 조합 / SILVER III / 44ms

import sys
import math


n, m = list(map(int, sys.stdin.readline().strip().split()))

# nCr = n(n-1)(n-2) ... (n-r+1) / r!
#     = n! / { r! * (n-r)! }

print(int(math.factorial(n) // (math.factorial(m) * math.factorial(n-m))))



'''
NOTE:

처음엔 답을 구할 때 나눗셈으로 했는데 오답 처리가 되었다.
나는 시간 초과를 걱정했는데... 오답 처리가 돼서 당황했다ㅜ
알고 보니까 부동소수점에 의해 발생하는 계산 오차 때문이었다.

나는 나눗셈 이후 int 처리 하는 식으로 구현했는데,
이미 나눗셈 할 때부터 오차가 발생해서 그 후 int로 바꿔주면 늦는다고 한다

그래서 몫을 구하는 방식으로 바꾸니까 맞았당
'''