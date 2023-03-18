'''
/*문제 정보 */
2800번 - 괄호 제거
난이도 - 골드 5
/*결과*/
메모리 - 31256KB
시간 - 48 ms
코드 길이 - 991B
/*풀이 방법 */
입력 받은 값에서 괄호의 인덱스값을 짝을 지어 받아주고
조합을 이용해 답을 구해준다.
'''
import sys
from itertools import combinations

x = list(map(str, sys.stdin.readline().strip()))

stack =[]
pos = []    # 괄호의 위치를 저장해주는 리스트
answer = set()

for i, value in enumerate(x):
    if value == '(':
        stack.append(i)          # (가 나오면 스택에 인덱스 값 입력
    elif value == ')':                      # )가 나오면
        pos.append((stack.pop(), i))   # 이전에 나온 ( 의 인덱스 갑과 지금 인덱스값 pos 에 저장


for i in range (1, len(pos)+1):
    comb = combinations(pos, i)   # 괄호 위치 개수 별 조합
    for j in comb:       # 괄호 위치르 하나씩 꺼내와서
        target = list(x)      # temp는 리스트 x를 전체를 가르킴.
        for k in j:
            target[k[0]] = ''  # ( 괄호 지우기
            target[k[1]] = ''  # ) 괄호 지우기

        answer.add(''.join(target))             # answer 에다가 붙혀서 저장

for a in sorted(list(answer)):
    print(a)


'''
/*오답 노트*/
/*느낀 점*/
1. 처음에 괄호 쌍을 저장할 순 있을 것 같아도, 경우의 수만큼 따로 출력할 방법이 떠오르지 않았다.
2. 서치해서 itertools 패키지에서 combinations 을 알게 되었고 이용했다.
3.combinations 뿐만 아니라 enumerate를 익혔다. 인덱스값을 같이 필요로 할 대 좋은 것 같다.
4. 계속 런타임에러 뜬다...
5. 결구 찾아냄... in range 를 in 만 써놨었음... 진짜 이걸 하루종일 못찾은 나도 참...


'''