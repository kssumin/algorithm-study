'''
/*문제 정보 */
11055번 - 가장 큰 증가하는 부분 수열
난이도 - 실버 2
/*풀이 방법 */
연속되지 않아도 증가하는 수열이면 합에 포함이 되는 것을 보고 dp 라고 생각했다.
이중 반복문을 돌려 조건에 맞게 적어주었따.
'''
import sys
input = sys.stdin.readline

a = int(input())
alist = list(map(int, input().split()))

dp = [0] * a
dp[0] = alist[0]

for i in range(1, a):
    for j in range(i):
        if alist[i] > alist[j]:
            dp[i] = max(dp[i], dp[j] + alist[i])
        else:
            dp[i] = max(dp[i], alist[i])
print(max(dp))
'''
/*오답 노트*/
1. 이중 for 문을 돌릴 생각을 하지 못했다.
   반복문이 여러개 돌려야 하는 건 느꼈지만 while 을 사용해야하나 했다.
2. 조건에 따른 dp[i] 이 헷갈렸다. dp[j]인지 다른건지 아직도 다시 생각하면
   헷갈린다. 
/*느낀 점*/
매번 스터디 진행하면서 문제 풀 때마다 dp를 떠올렸지만 오랜만에 dp를 푸니 
너무너무 어렵다...
'''