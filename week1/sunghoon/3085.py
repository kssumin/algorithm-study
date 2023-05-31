'''
/*문제 정보 */
3085번 - 사탕 게임
난이도 - 실버 2
/*풀이 방법 *
브루트포스로 사탕의 위치를 바꿔주고 카운트를 하여 최댓값을 구한다.
위치를 바꿔주고 카운트를 했다면 다시 원상태로 돌려놓고 다시 위치를 바꿔줘야 한다.

이것도 계속 오답으로 뜬다...
'''
import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))

result = 0

def count1():
    global result
    for i in range(1,n):
        a = 1
        for j in range(1,n):
            if graph[j][i] == graph[j-1][i]:
                a += 1
                result = max(result, a)
            else:
                a = 1

        a = 1
        for j in range(1,n):
            if graph[i][j] == graph[i][j-1]:
                a += 1
                result = max(result, a)

            else:
                a = 1

for i in range(n):
    for j in range(n):
        if j + 1 < n:
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
            count1()
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]

        if i + 1 < n:
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]
            count1()
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]

print(result)
'''
/*오답 노트*/
/*느낀 점*/

'''