'''
문제 : 연속합 (1912번)
난이도 : 실버2


점화식 (인터넷 서치함,,,)
: dp[n] = max(dp[n-1]+ arr[n], arr[n])

- 직전까지의 연속합 dp[n-1]이 양수인 경우에는 n번째 원소(arr[n])까지 더한 값이 최댓값
- 직전까지의 연속합이 음수인 경우에는 n번째 원소만 있는 경우가 최댓값

점화식에 맞는 코드를 작성해보자~

dp는 정말 점화식만 잘 찾으면 엄청 쉬워진다!
근데 점화식 찾기가 너무 어렵다ㅜㅜ
'''
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [0] * n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(dp[i-1]+arr[i], arr[i])
print(max(dp))
