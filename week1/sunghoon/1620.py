'''
/*문제 정보 */
1620 번 - 나는야 포켓몬 마스터 이다솜
난이도 - 실버 4
/*풀이 방법 */
딕셔너리로 저장을 하고 문제가 이름으로 올지 숫자로 들어올지 모르기 때문에
딕셔너리를 number, name 두개를 만들어 놓고 입력 받을 때 마다 각각에 저장해 주었다.
'''
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
number = {}
name = {}

for i in range(1, n + 1):
    monster = input().rstrip()
    name[monster] = i
    number[i] = monster

for i in range(m):
    a = input().rstrip()
    if a.isdigit():
        print(number[int(a)])
    else:
        print(name[a])

'''
/*오답 노트*/
/*느낀 점*/
1. 입력 받은 값을 name이랑 monster에 반대로 넣어줘서 초반에 자꾸 틀렸다..
2. 잘 나오길래 채점하니 시간초과.. 떠서 sys.stdin.readline 적어줌 그러니 이제 실행이 안됨
3. a= input()에 rstrip을 붙히니 실행은 되나 런타임 에러 살려주삼 
4. 첫 for 문에도 넣으니 성공 ....
'''