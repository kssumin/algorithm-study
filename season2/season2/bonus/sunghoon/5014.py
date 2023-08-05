'''
/*문제 정보 */
5014번 - 스타트링크
난이도 - 실버 1
/*풀이 방법 */
# bfs 로 풀었다. visit 로 횟수 카운트와 방문 표시를 동시에 해주었다.
'''
import sys
from collections import deque

def bfs(s):

    queue = deque()
    queue.append(s)  # 큐에 지금 위치 입력
    visit[s] = 1     # 지금 위치 방문 처리
    while queue:

        x = queue.popleft()

        if x == g :
            return visit[x] - 1     # 처음에 방문표시 한 값 빼주기

        else:
            for i in (x+u, x-d):
                if 0 < i  < f + 1:
                    if visit[i]:      # 방문했었다면 밑에 과정 생략
                        continue
                    queue.append(i)
                    visit[i] = visit[x] + 1   # 카운트 +1 해주기

    return "use the stairs"     #


f,s,g,u,d = map(int, input().split())

visit = [0 for _ in range(f + 1)]
print(bfs(s))

'''
/*오답 노트*/
처음에 함수 정의를 하지않고 방문처리랑 카운트를 따로해서 푼 문제가 있었는데 오답
이 나왔었다. 왜인지는 코드가 사라져서 결국 못찾았다...
큐랑 함수 정의하는게 익숙하지 않아서 그냥 작성했었는데 막상하니까 예전과 다르게
어렵지 않게 느껴졌다. 그렇다고 쉬운건 아니다.. 
/*느낀 점*/

'''