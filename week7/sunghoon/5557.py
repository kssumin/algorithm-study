'''
/*문제 정보 */
5557번 - 1학년
난이도 - 골드 5
/*풀이 방법 */
https://ddiyeon.tistory.com/59
코드 리뷰 했습니다.
dp 테이블의 구성을 가로를 0 ~ 20, 세로를 수식의 숫자를 순서대로 설정.
각 줄 마다 각 숫자를 더하거나 뺀 숫자의 경우의 수를 다음 줄에 저장.
각줄에 저장된 숫자의 의미는 i번 째 숫자까지 계산해 j를 만들 수 있는 경우의 수.
'''
N = int(input())

nums = list(map(int, input().split()))

dp = [[0]*21 for i in range(N-1)]
dp[0][nums[0]] = 1

for i in range(1, N-1):
    for j in range(21):
        # 뺐을 때, 0보다 작지 않을 때
        if j-nums[i]>=0: dp[i][j-nums[i]] += dp[i-1][j]
        # 더했을 때, 20보다 크지 않을 때
        if j+nums[i]<=20: dp[i][j+nums[i]] += dp[i-1][j]
print(dp[-1][nums[-1]])

'''
/*오답 노트*/
import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
answer = l[-1]
del l[-1]
sum = l[0]

count = 0

for i in range(1,len(l)):
    if sum >= l[i]:
    
누가봐도 1차원으로 풀 수 없을 거 같아서..... 포기 했습니다...
/*느낀 점*/
2차원 배열되면 생각보다 너무 어렵게 느껴진다... 
'''