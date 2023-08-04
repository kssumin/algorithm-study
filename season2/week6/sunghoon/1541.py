'''
/*문제 정보 */
1541번 - 잃어버린 괄호
난이도 - 실버 2
/*풀이 방법 */
주어진 식을 -로 나눈 뒤, 나눈 것들의 게산 값을 리스트에 저장
리스트 첫번 째 값에서 나머지 값을 계속 빼주는 식으로 구한다.
'''
import sys
input = sys.stdin.readline

x = input().split('-')
count = 0
sum1 = []
for i in x:
  y = i.split('+')
  for j in y:
    count += int(j)
  sum1.append(count)
  count = 0

result = sum1[0]
for k in range(1,len(sum1)):
    result -= sum1[k]

print(result)
'''
/*오답 노트*/
이중 for 문에서 들여쓰기를 잘못해서 틀렸었다... 
/*느낀 점*/

'''