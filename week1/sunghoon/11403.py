'''
/*문제 정보 */
11403번 - 경로 찾기
난이도 - 실버 1
/*풀이 방법 */
주제에 대해 감이 안잡혀 검색해 보았는데 플로이드 와샬을 알게되어
그 개념을 익히고 플로이드 와샬 알고리즘으로 풀었다.

'''
import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

for row in graph:
    for a in row:
        print(a, end = " ")
    print()


'''
/*오답 노트*/
/*느낀 점*/
이 문제를 풀 때, 에제를 보며 문제를 이해하는데 어려움이 있어 인터넷을 찾았었다.
처음에는 어떻게 값을 저장하고 출력을 할까 너무 걱정이 많았는데 생각보다 간단했다.

플로이드 워셜 알고리즘 자체는 다른 알고리즘에 비해 쉬운데, 3중 for 문에서 중간에 걸치는
k 가 가장 상위 단계 for 문 이어야 누락이 되지 않는다고 하는데 이번 발표에서 간단하게
알아봐야 겠다.
'''