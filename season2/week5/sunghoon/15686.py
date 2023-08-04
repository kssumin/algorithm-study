'''
/*문제 정보 */
15686번 - 치킨 배달
난이도 - 골드 5
/*풀이 방법 */
집과, 치킨 집의 위치를 저장한 후, 각각의 치킨거리를 계산 후
조합을 이용해 최소 치킨 거리를 선택한다.

'''
import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
result = float('inf')

home = []
chicken = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            home.append([i,j])
        if line[j] == 2:
            chicken.append([i,j])

for comb in combinations(chicken, m):
    sum_distance = 0
    for r1, c1 in home:
        distance = float('inf')
        for r2, c2 in comb:
            distance = min(distance, abs(r1-r2) + abs(c1 -c2))
            sum_distance += distance
            result = min(result, sum_distance)

print(result)

'''
/*오답 노트*/
일단 처음 문제를 풀 때, 맵을 받는 것 까지 쉽게 했다.
그다음 조합을 사용해야 한다는 것을 알고는 있지만, 어떻게 2의 위치를 찾아낼까
생각을 해봤는데, bfs 나 dfs 로 x,y 좌표fmf 옮겨가면서 찾는게 떠올랐다.
자신이 없어 인터넷을 찾아봤는데 내 생각과 다르게 이중 for문으로 간단하게 집,치킨집
위치를 저장할 수 있었다...
인터넷 참고해서 작성했는데 계속 오답이다 ㅠㅠ
/*느낀 점*/

'''