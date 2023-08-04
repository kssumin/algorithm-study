'''
/*문제 정보 */
2644번 - 촌수계산
난이도 - 실버 2
/*풀이 방법 */
DFS 로 시작점에서부터 +1 증가시켜 촌수 관계를 저장하고
출력하려는 값이 촌수관계가 있으면 출력 없으면 -1
'''
import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline

def dfs(a):
    for i in graph[a]:
        if result[i] == 0:
            result[i] = result[a] + 1
            dfs(i)

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = [0] * (n+1)

dfs(a)

if result[b] > 0:
    print(result[b])

else:
    print(-1)




'''
/*오답 노트*/
/*느낀 점*/
사소한 오타와 잘못된 변수 입력으로 시간이 꽤 걸렸다.
주제가 DFS 라고 적혀있지 않아 DFS 를 떠올리는데 시간이 꽤 걸렸다.
'''