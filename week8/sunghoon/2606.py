'''
/*문제 정보 */
2606번 - 바이러스
난이도 - 실버 3
/*풀이 방법 */
dfs로 연결 되어있는 곳을 방문하여 방문처리를 해주었다.
'''
import sys
input = sys.stdin.readline

c = int(input())
s = int(input())
graph = [[]for _ in range(c+1)]
visited = [0] * (c+1)

for i in range(s):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x):
    visited[x] = 1
    for j in graph[x]:
        if visited[j] == 0:
            dfs(j)

dfs(1)
print(sum(visited)-1)
'''
/*오답 노트*/
def dfs(x):
    count = 0
    visited[x] = 1
    for j in graph[x]:
        if visited[j] == 0:
            dfs(j)
            count += 1
        
count 변수 설정을 dfs 함수 내에서 해도 오류, 밖에서 해도 오류가 나길래
인터넷으로 다른 사람들 답을 찾아보니 visited 합으로 답을 출력한 걸을 가져왔다.
변수 설정에 관해서도 한번 찾아봐야 할 것 같다.
/*느낀 점*/
매번 2차원 리스트를 풀 때마다, 머리가 복잡해져 인터넷에 있는 이미지를 보며
다시 확인하게 된다....
'''