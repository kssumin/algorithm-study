'''
/*문제 정보 */
1697번 - 숨바꼭질
난이도 - 실버 1
/*풀이 방법 */
5014와 같은 방식으로 풀었다.
'''
import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append(n)

    while queue:

        x = queue.popleft()
        if x == k :
            return visited[k]
        else:
            move = [x + 1, x - 1, 2 * x]
            for i in move:
                if 0 <= i <= 100000 and not visited[i]:
                    queue.append(i)
                    visited[i] = visited[x] + 1

n, k = map(int, input().split())

visited = [0] * (100001)

print(bfs())

'''
/*오답 노트*/
1. 처음에 런타임 에러가 뜬 이유는 i에 대한 조건을 달아주지 않아서였다.
    if 0 <= i <= 100000 and not visited[i]:
    조건을 달아주지 않으면 visited의 범위를 넘어가는 경우가 발생한다.
    예제는 맞게 나오는데 런타임 에러가 나오면 대부분 범위에서 문제가 
    생겼던 것 같다.
2. visited 의 범위를 처음에 n과 k 중 큰값 +1 만큼 했었는데, 좀 복잡해져서
   문제에서 주어진 범위만큼 해도 되는 문제였다.
/*느낀 점*/

'''