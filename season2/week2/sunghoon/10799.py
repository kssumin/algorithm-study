'''
/*문제 정보 */
10799번 - 쇠막대기
난이도 - 실버 2
/*결과*/
메모리 - 32472KB
시간 - 64ms
코드 길이 - 894B
/*풀이 방법 */
입력 받은 값을 스택 리스트에 차례로 넣어 경우의 수에 따라 막대기 개수 카운트
'''
import sys
input = sys.stdin.readline

x = list((input()))
del x[-1]  # 리스트에 공백 /n 생기는거 삭제 시켜줌

stack = [] # 스택 리스트
count = 0  # 막대기 개수

for i in range(len(x)):
    if x[i] == '(':
        stack.append(x[i])   # '('일 경우에는 스택에 넣어줌.

    else:                        # 지금 넣어주는 값은 ')'
        if x[i-1] == '(':
            stack.pop()          # 이전 넣어준 값이 '('이면 레이저 이고 제거해줌
            count += len(stack)  # stack 값은 쌓인 '(' 뿐이므로 그 개수만큼 막대기 카운트

        else:                   # 이전 값이 ')' 이고 현재 값도 ')' 인경우는 한 막대기의 끝부분이므로
            stack.pop()         # 도막이 끝이 난 막대기를 없애주고
            count +=1           # 카운트는 +1 만 해주면 됨.

print(count)



'''
/*오답 노트*/
/*느낀 점*/
"""
stick = [0 for _ in range(len(x))]  # 막대기 위치 저장 리스트
bim = [0 for _ in range(len(x))]  # 레이저 위치 저장 리스트 /근데 변수 이름 하려다가 안되네

stack = []*len(x)
stack[0] =x[0]
for i in range(1,len(x)):
    stack.append(x[i])  # test 리스트에 첫 값은 넣어놓기
    if stack[i-1] == "(" and x[i] == ")":
        bim[i-1] = 1
        bim[i] = 1      # 레이저 위치 찾아서 적어주기
        del stack[i-1]
        del stack[i]    # 스택 리스트 삭제
"""
1. 처음에 너무 복잡하게 생각했다. 이전 문제 풀이와 비슷하게 생각했던 것 같다.. 
   카운트를 간단하게 셀 수 있는 방법을 찾아냈다...
2. 문제의 경우의 수와, 규칙? 등을 실제로 적어서 해보면 코드 작성할 때 더 효율적인 것 같다.!

'''