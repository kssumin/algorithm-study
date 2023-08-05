import sys
input = sys.stdin.readline


def check(v):
    go_list = []
    visited = [False for _ in range(N)]
    for v1 in range(N):
        if graph[v1][v] == 1:
            go_list.append(v1)
    while go_list:
        v2 = go_list.pop()
        graph[v2][v] = 1
        for v3 in range(N):
            if graph[v3][v2] and not visited[v3]:
                go_list.append(v3)
                visited[v3] = True


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
for i in range(N):
    check(i)
for i in range(N):
    print(*graph[i])

"""
풀이 :
graph 가 있으면 0부터 N - 1 부터 차례로
(0, 0), (1 ,0), (2, 0) ··· 처럼 세로로 탐색한다.
탐색하다가 (i, j)에서 1이 나오면 i를 go_list에 추가한다.
탐색이 끝난 후, for문으로 go_list를 돌면서 i행을 탐색한다. i행을 탐색하다가 1이 나오면 그 숫자 또한 j열을 갈 수 있다는 뜻이니
graph[i][j]를 1로 만들고 방문처리한다.

다른 사람들 풀이를 보니 다른 사람들은 세로로 탐색한 것이 아니라 전부 가로로 탐색했다.
a -> b, b -> c 로 길이 이어져있다면
가로 : a -> b로 갈 수 있으니 b가 갈 수 있는 길을 찾아낸다. b -> c이므로 a -> c도 가능
세로 : b -> c로 갈 수 있으니 b로 올 수 있는 길을 찾아낸다. a -> b이므로 a -> c도 가능
이 차이가 있다.
나는 세로로 탐색했는데 다른 사람들이 훨씬 쉽게 푼 것 같다.
다음에 풀 땐 더 쉬운 방법이 있나 찾아봐야겠다...
굳이 따지자면 dfs로 풀었다.
"""