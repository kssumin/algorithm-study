'''
/*문제 정보 */
2217번 - 로프
난이도 - 실버 4
/*풀이 방법 */
로프가 견딜 수 있는 무게를 내림차순으로 정렬 후, 1 ~ n 개를 골랐을 때, 인덱스 값과 곱해줘
최대값을 갱신해서 구해준다.
'''
import sys
input = sys.stdin.readline

n = int(input())
rope = []

for i in range(n):
    r = int(input())
    rope.append(r)

result = 0

rope.sort(reverse = True)

for i in range(n):
    result = max(result, rope[i] * (i+1))

print(result)
'''
/*오답 노트*/
/*느낀 점*/
내림차순으로 정렬 후 반복문으로 인덱스값을 불러와 쉽게 답을 구했을 때, 신기했당..
'''