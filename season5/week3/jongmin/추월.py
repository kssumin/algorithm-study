#2002번
from itertools import combinations as comb
N = int(input())

daegeun = {}
youngsik = {}

cnt = 0

for i in range(N):
    daegeun[input()] = i+1

for i in range(N):
    youngsik[input()] = i+1

for i in daegeun.keys():
    # youngsik - daegeun 이 0보다 작다면,
    # 들어갈 때 보다 나갈 때 더 빨리 나간 것이므로
    # 추월했다고 볼 수 있다.
    print(i, youngsik[i] - daegeun[i])
    if youngsik[i] - daegeun[i] < 0:
        cnt += 1

print(cnt)