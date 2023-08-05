import sys
input = sys.stdin.readline
num = int(input())
dp = [1 for _ in range(num+1)]
for i in range(2, num+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746
print(dp[num])

"""
처음 문제를 보고 피보나치 수열이랑 같아서 dp로 구현했었다.
그런데 메모리 초과가 뜨길래 메모리를 덜 쓰고 시간은 오래 걸리는 재귀함수로 짜 봤다.
그런데 이번엔 또 RecursionError가 떴다. 그래서 게시판을 찾아보고
dp에 저장할 때 미리 15746으로 나눈 값을 저장했더니 답이 나왔다.
만약 c가 충분히 크다면 (a + b)를 c로 나눈 나머지나 a를 c로 나눈 나머지 + b를 c로 나눈 나머지가 같기에
숫자 크기를 줄이기 위해서 6번째 줄과 같이 코드를 짜야했다.
"""