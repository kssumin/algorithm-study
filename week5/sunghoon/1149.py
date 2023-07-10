'''
/*문제 정보 */
1149번 - RGB 거리
난이도 - 실버 1
/*풀이 방법 */
최솟값 구하는 문제라 dp가 바로 떠올랐다.
리스트에 rgb 를 받아주고 이전 값에서 계속 최솟값을 갱신해
마지막에서 가장 최솟값을 출력
'''
import sys
input = sys.stdin.readline

n = int(input())
house = []

for i in range(n):
    house.append(list(map(int, input().split())))

for i in range(1,n):
    house[i][0] += min(house[i-1][1],house[i-1][2])
    house[i][1] += min(house[i-1][0],house[i-1][2])
    house[i][2] += min(house[i-1][0], house[i-1][1])

print(min(house[-1]))

'''
/*오답 노트*/
/*느낀 점*/
다른 dp 문제 처럼 데이터 저장하는 곳과 dp 리스트를 따로 만들어
주어 푸려다가 그렇게 하지 않아도 되는 것을 알게 되었다.
이제 주제는 떠오르나 적용에서 힘이 든다.
'''