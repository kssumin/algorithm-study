'''
/*문제 정보 */
17626번 - Four Squares
난이도 - 실버 3
/*풀이 방법 */
dp 에 1부터 n 까지의 모든 dp 값을 구해준다.
dp 값을 구할 때 모든 제곱 수를 비교해 최솟값을 넣어준다.
'''
import sys
input = sys.stdin.readline

n = int(input())
count = 0
dp = [0 for _ in range(n+1)]   # dp[i] 는 i를 만들기 위해 사용된 제곱의 수

a = 1
while a** 2 <= n:    # n보다 작은 제곱수의 dp 값을 1로 저장해 줌
    dp[a**2] = 1
    a +=1

for i in range(1,n+1):
    if dp[i] != 0:           # 이미 넣어준 값들은 건너뛰기
        continue

    j = 1
    while j*j <= i:
        if dp[i] == 0:     # dp 값이 없다면 값을 넣어준다.
            dp[i] = dp[j * j] + dp[i - j * j]
        else:              # dp 값을 넣어준 뒤에도 다른 제곱수를 넣어 비교해 최솟값을 저장
            dp[i] = min(dp[i], dp[j * j] + dp[i - j * j])
        j += 1


print(dp[n])


'''
/*오답 노트*/
풀이 1
while True:
    if n == 0:
        break
    if a ** 2 == n:
        count += 1
        n -= a**2
        a = 1
        continue

    elif a ** 2 < n:
        a += 1
        continue
    else:
        a -= 1
        n -= a**2
        count += 1
        a = 1
        continue
        
처럼 a를 계속 1씩 더해 제곱값이 n보다 커질 때 그 전 a값의 제곱을 빼주는 식으로 했는데 
오답이 나온다..

/*느낀 점*/
인터넷에서 이론을 봤는데, 이해는 했으나 코드로 적기에 딱히 떠오르지 않아
dp로 풀었다.. dp가 난이도에 비해 어렵게 느껴진다.
'''