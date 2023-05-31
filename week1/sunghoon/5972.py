'''
/*문제 정보 */
5972번 - 택배 배송
난이도 - 골드 5
/*풀이 방법 */
dp? dfs? bfs? 어디서 본 유형인데... 일단 예제는 맞는데
메모리 초과... 딱 봐도 안될 것 같긴 했다...
'''
import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())

graph = [[INF]*(m+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

result = [INF] * (n+1)
result[1] = 0

def dfs(a):
    for i in range(1,m+1):
        if graph[a][i] < 1001:
            result[i] = min(result[a] + graph[a][i], result[i])

for j in range(1,n+1):
    dfs(j)

print(result[n])




'''
/*오답 노트*/
/*느낀 점*/

'''