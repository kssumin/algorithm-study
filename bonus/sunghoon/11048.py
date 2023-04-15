'''
/*문제 정보 */
11048번 - 이동하기
난이도 - 실버 2
/*풀이 방법 */
입력 받은 값을 저장해주고, dp를 만들어 최댓값을 매번 갱신 해준다.
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(n):
    li = map(int, input().split())
    graph.append(list(li))


for x in range(1, n+1):
    for y in range(1,m+1):
        dp[x][y] = graph[x-1][y-1] + max(dp[x][y-1], dp[x-1][y],dp[x-1][y-1])

print(dp[x][y])
'''
/*오답 노트*/
/*느낀 점*/
약간 이런 문제 풀 때, +1 씩 해서 푸는게 개인적으로 더 복잡하다 생각해서 그냥 받은
변수 만큼 범위 정해서 풀었는데 dp 최댓값 갱신할 때 오류 문제나 더 복잡해지는 것 같아
+1 씩 하니 쉽게 풀 수 있었다.
'''