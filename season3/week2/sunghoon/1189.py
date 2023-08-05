'''
/*문제 정보 */
1189번 - 컴백홈
난이도 - 실버 1
/*풀이 방법 */
dfs 로 시작점에서 출발해 .인 경우 카운트 하나씩 해가면 도착지점에서 k 값과 카운트값이
값으면 result 값을 +1 해주었다.

'''
import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(list(input().rstrip()))

result = 0

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x,y,count):
    global result

    if x == 0 and y == c-1 and count == k:
        result += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == '.':
                arr[nx][ny] = 'T'
                dfs(nx, ny, count+1)
                arr[nx][ny] = '.'

arr[r-1][0] = 'T'
dfs(r-1, 0, 1)
print(result)
'''
/*오답 노트*/
/*느낀 점*/
dfs 는 생각만해서 푸는 것보다 종이에 적어서 하는 편이 확실히 이해도 빠르고 코드작성이
빨라지는 것 같다.
'''