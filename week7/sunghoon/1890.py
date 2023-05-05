'''
/*문제 정보 */
1890번 - 점프
난이도 - 실버 1
/*풀이 방법 */
주어진 값을 받아주고 dp를 만들어 주어 시작값을 1로 하고 반복문을 돌려
이동한 곳에 이동하기 전 위치에 값을 더해주는 것을 반복해 dp[-1][-1]를 출력해줌
'''
import sys
input = sys.stdin.readline

n = int(input())
map1 = []
for i in range(n):
    l = list(map(int, input().split()))
    map1.append(l)


dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n -1:
            break

        move = map1[i][j]

        if i + move < n:
            dp[i + move][j] += dp[i][j]

        if j + move < n:
            dp[i][j + move] += dp[i][j]

print(dp[-1][-1])
'''
/*오답 노트*/
오답 1
for i in range(n):
    for j in range(n):

        move = map1[i][j]

        if i + move < n:
            dp[i + move][j] += dp[i][j]

        if j + move < n:
            dp[i][j + move] += dp[i][j]
에제를 넣어보니 12라는 값이 나와서 왜일까 생각해 보았는데 마지막 돌 때,
if 문 두개가 작동되어 생각한 값보다 4배 더 크게 나왔었다. 그래서 
break를 걸어주었다. 
/*느낀 점*/

'''