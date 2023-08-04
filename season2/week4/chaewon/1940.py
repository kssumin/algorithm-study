# BJ 1940 : 주몽 / SLIVER IV / 2264ms

import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

meterials = list(map(int, sys.stdin.readline().strip().split()))

cnt = 0
for i in meterials:
    j = m - i
    if j in meterials:
        cnt += 1

print(int(cnt / 2))
# 2로 나누어주는 이유
# ex) m = 9, meterials = [2, 7, 4, 1, 5, 3] 일 때
#     (i, j)가 (2, 7)일 때, (7, 2)일 때 모두 cnt값이 증가함



'''
NOTE:

재료들의 고유값에 중복된 값이 들어올 경우까지 고려해야 하는 줄 알았다ㅠ
그거 때문에 dictionary도 사용해보고 좀 애를 먹었는데

일단 단순하게 접근해보려고 중복값은 없다는 전제로 코드를 짜고 돌렸더니
정답 처리 되었다!! 문제가 애매하군

'''