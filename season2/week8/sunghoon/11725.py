'''
/*문제 정보 */
11725번 - 트리의 부모 찾기
난이도 - 실버 3
/*풀이 방법 */
dfs 로 1 부터 graph 를 돌아서 parent 에 부모 노드 번호를 저장해 주었다.
graph[a] = [b] 라면 parent[b] = [a] 식으로 저장해주었다.
방문처리를 하여 parent 에 저장하는데 오류가 나지 않게 하였다.
'''
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
parent = [0] * (n+1)

for i in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    visited[x] = 1
    for i in graph[x]:
        if visited[i] == 0:
            parent[i] = x
            dfs(i)

dfs(1)
for j in range(2, n+1):
    print(parent[j])


'''
/*오답 노트*/
처음에는 반복문으로 찾아야 할 값 i 를 주고 graph[1] 에서부터 dfs 로 재귀를
사용해 부모 노드를 찾으려 했는데, 복잡해 질 것 같아서 parent 리스트를 만들어
graph 를 진작에 다 돌아 parent 에 저장해 준 뒤 값을 찾아내는 방식으로 했다.
/*느낀 점*/
RecursionError: maximum recursion depth exceeded in comparison
라는 오류가 떴었는데, 내가 처음에 dfs를 작성하는데 오류가 난 줄 알고 검색해보니
파이썬에서 재귀 호출 횟수를 제한하고 있어 나는 오류라고 한다.
sys 모듈에서 setrecursionlimit 함수를 사용해 깊이를 늘려주어 해결 할 수 있었다.
'''