'''
/*문제 정보 */
16953번 - A → B
난이도 - 실버 2
/*풀이 방법 */
b 를 a 로 바꿔주는 것이 더 쉬울 것 같아 반복문으로 조건을 걸어줘서 카운트를 해주었다.
'''
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

count = 1

while True:
    if b == a:
        break
    elif (b < a) or (b % 10 != 1 and b % 2 != 0):
        count = -1
        break
    else:
        if b % 10 == 1:
            b //= 10
            count += 1
        else:
            b //= 2
            count += 1

print(count)
'''
/*오답 노트*/
/*느낀 점*/
문제 자체가 여럽게 느껴지지는 않았는데 수많은 오답과 시간초과, 런타임 에러가 걸렸었다..

'''