'''
/*문제 정보 */
1918번 - 후위 표기식
난이도 - 골드 2
/*결과*/
메모리 - 31256 KB
시간 - 40ms
코드 길이 - 721 B
/*풀이 방법 */
우선순위를 메겨 조건을 설정해 풀었다.
'''
import sys

l = list(sys.stdin.readline().rstrip())   # 식 입력 받기
stack = []
ans = ''      # 출력해야하는 값
for i in l:
    if i.isalpha():
        ans += i        # 알파벳이면 바로 ans 에 저장

    else :
        if  i == '(':         # 우선 순위 1순위
            stack.append(i)     # 괄호는 ans에 들어가면 안되고 stack에 저장

        elif i =='*' or i == '/':    # 우선 순위 2 순위
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()       # 자신보다 먼저 들어가 있던 *, /를 ans에 저장
            stack.append(i)              # 먼저 들어가 있던 애들을 빼내고 본인이 들어감

        elif i =='+' or i == '-':         # 우선 순위 3순위
            while stack and stack[-1] != '(':
                ans += stack.pop()         # (가 나오기 전까지 값들을 ans 에 보냄

            stack.append(i)                # 그 후 본인이 stack에 들어감

        elif i == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()         # (가 나오기 전까지 값들을 ans 에 보냄
            stack.pop()                    # 괄호 안에 값을 다 내보내고 괄호도 처리함
while stack:
    ans += stack.pop()                     # stack에 저장된 값 다 털어내기

print(ans)
'''
/*오답 노트*/
/*느낀 점*/
1. 처음에 런타임 에러가 떴다. 첫 코드에서 (를 받아주자 마자 스택에서 빼는 
   코드를 작성했는데, 복잡해지면서 오류가 나 것 같다. 그 이후에는 )를 받았을 때 
   스택에서 (가 나오기 전까지 값들을 다 받아주다가 (가 나오면 없애는 방식으로 바꿨다.

2. 처음에 ans +=stack[-1] 로 값을 받아 줬는데 시간초과가 떴고.
   ans +=stack.pop()로 바꿔주니 정답 처리 되었다.
   
3. 확실히 머리로만 생각하는 것보다 직접 종이에 그려서 해보는게 도움이 되었다.
   '''