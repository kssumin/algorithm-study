'''
/*문제 정보 */
1654번 - 랜선 자르기
난이도 - 실버 2
/*풀이 방법 */
필요한 랜선 수를 충족할 때의 길이를 이분탐색으로 구했다.
'''
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
line = []

for _ in range(k):
    line.append(int(input()))

start = 1
end = max(line)

while start <= end:
    mid = (start + end) // 2
    result = 0
    for i in line:
        result += i // mid

    if result >= n:
        start = mid + 1

    else:
        end = mid - 1

print(end)
'''
/*오답 노트*/
while start <= end:
채점 돌리자마자 오답으로 나오길래 코드를 보니 while 조건을 잘못 걸었었다.
/*느낀 점*/
뭔가 문제 처음 읽었을 때 는 어렵다고 생각했는데 난이도 보고 편하게 
이분탐색 적용하니 쉽게 풀 수 있었다.
'''