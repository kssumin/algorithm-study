'''
/*문제 정보 */
12919번 - A와 B 2
난이도 - 골드 5
/*풀이 방법 */
T를 S로 바꾸는 식이 더 쉬울 것 같아서 T를 S 를 바꾸는 식으로 함수를 사용했다.
'''
import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

def aba(x):
    if x == s:
        return 1

    if len(x) == 0:
        return 0
    if x[-1] == 'A':
        del x[-1]
        aba(x)

    if x[-1] == 'B':
        del x[-1]
        reversed(x)
        aba(x)

print(aba(t))
'''
/*오답 노트*/
/*느낀 점*/
인덱스 에러가 뜬다... 풀지 못했다...
'''