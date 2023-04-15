import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N :
            if graph[nx][ny] > tmp and result_graph[nx][ny] == 'X':
                result_graph[nx][ny] = 'O'
                dfs(nx, ny)
    return

N = int(input())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_num = 0
for _ in range(N):
    row = list(map(int, input().split()))
    graph.append(row)

for tmp in range(101):
    result_graph = [['X' for _ in range(N)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if result_graph[i][j] == 'X' and graph[i][j] > tmp:
                count += 1
                result_graph[i][j] = 'O'
                dfs(i,j)
    if count == 0:
        break
    else:
        max_num = max(max_num, count)

print(max_num)
"""
처음에 문제를 내 맘대로 해석해서 몇 번 틀렸다.
장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력해야 하므로 비의 양을 1부터 끝까지 넣어보고 최대 개수를 알아내는 건데
예제만 보고 "비의 양이 N이나 N-1만큼 왔을 때 안전한 영역의 개수를 출력하는 건가?" 생각했다.
항상 문제를 제일 잘 봐야하는데 빨리 풀려고 대충 보게 된다... 

옛날에 풀었던 배추 문제랑 비슷해서 보여서 처음 풀이에서는 잠긴 지역을 X, 잠기지 않은 지역을 O로 바꾼 다음 bfs로 따로 떨어져 있는 지역의 개수를 세게 했다.
그런데 제출하고 나니 다른 사람들의 코드랑 시간이 2배 정도 되어서 풀이를 바꾸었다.

잠긴 지역과 잠기지 않은 지역들을 O, X로 만들면서 시간이 오래 걸리나 했는데 그것이 문제가 아니였다.
11번쨰줄에 result_graph[nx][ny] = 'O' 이걸 안 써서 시간이 굉장히 오래 걸리는 것이었다.
없어도 되는 문장이긴한데 저 문장이 있어야 필요 없는 방문을 없애준다. 저번에도 이것때문에 정답은 맞지만 시간이 오래 걸렸던 것 같은데 문제를 많이 풀어봐야겠다.

시간을 줄이려는 과정에서 다른 사람 코드를 참고했는데 이상한 코드가 있어서 살펴봤더니 테스트 케이스들이 이상하다는 걸 알았다.
내가 본 사람의 코드에서는 전체 지역 중 최대 높이를 구한 다음 비의 양을 그 높이만큼만 대입해서 비교하는 코드였다.
그런데 그 사람이 전체 지역 중 최대 높이를 구할 때 maxH = max(max(graph))라는 코드를 작성했는데
이 코드는 모든 테스트 케이스들에서 최대값이 있는 행의 첫 번째값이 모든 행의 첫 번째 값 중에서 가장 큰 수이어야만 최대 높이를 제대로 구할 수 있다.
"""

