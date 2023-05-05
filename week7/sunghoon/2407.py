'''
/*문제 정보 */
2407번 - 조합
난이도 - 실버 3
/*풀이 방법 */
굳이 dp로 안풀었다...
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())


a = 1
b = 1
for i in range(n,0,-1):
    a *= i

for j in range(m,0,-1):
    b *= j
for k in range(n-m,0,-1):
    b *= k

print(a//b)


'''
/*오답 노트*/
/*느낀 점*/
나누기, 몫 매번 헷갈려서 계속 검색해서 풀었다..
'''