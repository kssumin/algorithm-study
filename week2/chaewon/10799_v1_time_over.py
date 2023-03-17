# BJ 10799 : 쇠막대기 / SILVER II /

import sys

# 괄호 입력 받기
bracket = sys.stdin.readline().strip()

# '()'는 레이저에 해당하므로 이를 '1'로 변경함
bracket = bracket.replace('()', '1')

# 입력받은 괄호와 '1'을 list로 저장
brk_list = list(bracket)

cnt = 0
stack = []

for i in brk_list:

    # pop_list 초기화
    pop_list = []

    # brk_list에 있는 i를 stack에 넣어줌
    stack.append(i)

    # stack에 넣는 값이 ')'라면, 괄호 쌍이 이루어졌다는 뜻이므로
    if i == ')':

        # pop_list에 stack.pop한 값들을 추가 - stack.pop된 값으로 '('이 나올 때까지
        while 1:
            pop_list.append(stack.pop())
            if pop_list[-1] == '(':
                break

        # 레이저의 개수를 카운트
        n = pop_list.count('1')

        # pop_list 안에 들어있는 값은 오직 레이저 n개를 포함한 괄호 한 쌍
        # 이때 절단 후 생기는 막대기의 개수는 n+1
        cnt += (n+1)

        # n개 만큼 stack에 '1'을 다시 추가 -> 레이저의 개수와 위치를 유지해주어야 함
        for _ in range(n):
            stack.append('1')

print(cnt)



'''
NOTE:

시간초과가 나는데, 시간복잡도가 O(n^2)이라 그런 것 같다...
17번 라인의 for문에서 시간복잡도 O(n), 29번 라인의 while문에서 최악의 경우 O(n/2)의 시간복잡도가 나오는 것 같다ㅠ
pypy로 돌려봐도 시간초과가 나오는데, 아예 접근 자체를 잘못한 건가 싶기도 하다
정답은 아주 잘 나온다!!

'''