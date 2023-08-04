'''
/*문제 정보 */
2212번 - 센서
난이도 - 골드 5
/*풀이 방법 */
센서들의 위치를 오름차순으로 정렬 후 센서들 사이 간 거리를 구해
오름차순으로 정렬해 준다. 집중국의 수 k에서 -1 만큼 큰 값을 빼내주고
남은 거리들의 합이 정답이다.
'''
import sys
input = sys.stdin.readline


n = int(input())
k = int(input())
sensor = sorted(map(int, input().split()))

if n <= k:
    print(0)
    sys.exit(0)

distance = []
for i in range(0,n-1):
    dis = sensor[i+1] - sensor[i]
    distance.append(dis)

distance.sort()
for j in range(k-1):
    distance.pop(-1)

print(sum(distance))
'''
/*오답 노트*/
/*느낀 점*/
종이에 적어서 풀다보니 쉽게 풀 수 있었다..
'''