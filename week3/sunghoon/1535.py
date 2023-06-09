'''
/*문제 정보 */
1535번 - 안녕
난이도 - 실버 2
/*풀이 방법 */
https://sangminlog.tistory.com/entry/boj-1535
이 블로그를 보고 코드를 작성하였는데 블로그 코드는 정답
나는 틀렸습니다, 런타임 에러가 떴다.

dp 냅색 문제의 기본 개념은
i번 째 물건을 배낭에 넣을 수 없다면,
i -1 개의 물건들을 갖고 구한 전 단계의 값 가져오기

i번째 물건을 배낭에 넣을 수 있다면,
max(i -1 개의 물건들을 갖고 구한 전 단계의 값, i번째 물건만큼의 무게를 뺀 값 + i번 째 물건)
'''
import sys
input = sys.stdin.readline

n = int(input())
hp = list(map(int, input().split()))
happy = list(map(int, input().split()))

dp = [[0 for _ in range(100)] for _ in range(n)]

for i in range(n):
    for j in range(100):
        if hp[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-hp[i]] + happy[i])

        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][98])


'''
/*오답 노트*/
마지막 print(dp[-1][-1]) 로 놓으니 틀렸습니다.
print(dp[n][98]) 로 놓으니 런타임 에러가 떴다.
진짜 모르는 문제 블로그 보고 참고해서 풀 때 마다 정답으로 안나오면 미치겠다.
/*느낀 점*/

'''