'''
/*문제 정보 */
1904번 - 01 타일
난이도 - 실버 3
/*풀이 방법 */
점화식을 찾아서 구해주었다. 피보나치 수열이었다.
'''
import sys
input = sys.stdin.readline

n = int(input())

li = [0] * 1000001
li[0], li[1] = 1,2

for i in range(2, n):
    li[i] = (li[i-1] + li[i-2]) % 15746

print(li[n-1])
'''
/*오답 노트*/
오답 1 . 메모리 초과
import sys
input = sys.stdin.readline

n = int(input())

li = [0] * n
li[0], li[1] = 1,2

for i in range(2, n):
    li[i] = li[i-1] + li[i-2]

print(li[n-1] % 15746)

오답 2. 런타임 에러
li = [0] * n
li = [0] * 1000001 로해주니 정답
/*느낀 점*/
왜 나머지 처리를 정답을 출력할 때는 메모리 초과인데 for 안에서 매번
해주는 것은 메모리 초과가 되지 않을까 한번 알아봐야겠다.
'''