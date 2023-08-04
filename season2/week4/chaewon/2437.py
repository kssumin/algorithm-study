# BJ 2437 : 저울 / GOLD II / 40ms

import sys

n = int(sys.stdin.readline().strip())
weights = list(map(int, sys.stdin.readline().strip().split()))
weights.sort()

sum = 1

for num in weights:
    if sum < num:
        break

    sum += num

print(sum)

'''
NOTE:
아이디어 생각하는게 말도 안되게 어려웠다!!
결국 찾아봤는데 그래도 이해하는 데 꽤 걸린...ㅠ

num이 sum보다 작다면 num은 sum ~ (sum+num) 사이의 모든 수를 만들 수 있다.
num이 sum보다 크다면 sum+1이 만들 수 없는 최소의 수가 된다.

만약 무게가 1인 추가 없으면, 결과값이 1이 나와야 하는데
이 코드는 sum의 초기값이 1이기 때문에 그 조건까지 만족시킨다.

어렵다
'''