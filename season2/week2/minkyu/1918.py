import sys
input = sys.stdin.readline


def swap(str1, op, str2):
    return str1+str2+op


def put_both(string):
    return '(' + string + ')'


def find_left_right(index):
    # swap 할 문자열의 인덱스들을 알아내는 함수
    # ex) (A+B)*C --> (의 좌표, C의 좌표
    # 수식 기호 양쪽에 ()가 있음
    if expression[index - 1] == ')' and expression[index + 1] == '(':
        st = find(index, 'left')[0]
        ed = find(index, 'right')[1]
        return st, ed
    # 수식 기호 왼쪽에 ()가 있음
    elif expression[index - 1] == ')':
        return find(index, 'left')
    # 수식 기호 오른쪽에 ()가 있음
    elif expression[index + 1] == '(':
        return find(index, 'right')
    # 수식 기호 양 옆에 ()가 없음
    else:
        return index - 1, index + 1


def find(index, direct):
    # 괄호가 씌워질 양 끝 좌표를 알아내는 함수
    # index 에 수식의 인덱스가 저장돼 있고 direct 는 괄호가 왼쪽에 있는지 오른쪽에 있는지 나타냄.
    # ex) (A+B)*C --> index == 5, 방향 == left, (와 C의 좌표 return 0, 6
    if direct == 'left':
        op1 = ')'
        op2 = '('
    elif direct == 'right':
        op1 = '('
        op2 = ')'
    tmp_index = index
    stack = []
    while 1:
        if direct == 'left':
            tmp_index -= 1
        elif direct == 'right':
            tmp_index += 1
        if expression[tmp_index] == op1:
            stack.append(op1)
        elif expression[tmp_index] == op2:
            stack.pop()
            if not stack:
                break
    if direct == 'left':
        return tmp_index, index + 1
    elif direct == 'right':
        return index - 1, tmp_index


def open_left_right(string):
    # 괄호 안의 식을 푸는 함수
    # ex) (A+B) --> AB+, ((A+B)*C) -->(A+B)C*, (A+B)C* -->AB+C*
    stack = []
    for i in range(len(string)):
        letter = string[i]
        if letter == '(':
            stack.append('(')
        if letter == ')':
            stack.pop()
        # 만약 (가 열려 있고 그 다음에 문자가 오면
        if len(stack) == 1 and 42 <= ord(letter) <= 47:
            start, end = find_left_right(i)
            # 괄호가 씌워질 바로 왼쪽 좌표 ~ 수식 기호의 바로 왼쪽 == 수식 기호 왼쪽 식
            # 수식 기호의 바로 오른쪽 ~ 괄호가 씌워질 바로 오른쪽 좌표 == 수식 기호 오른쪽 식
            # 따라서 swap(수식 왼쪽 식, 수식 기호,  수식 기호 오른쪽 식)
            return string.replace(string[start-1:end+2], swap(string[start:i], expression[i], string[i+1:end+1]))
    # 괄호가 연속 두 개 있을 때
    # ex) ((A+B)) --> (A+B)
    return string[1:len(string)-1]


def find_symbol_put_both(symbol1, symbol2):
    # 괄호를 씌워주는 함수
    index = 0
    global expression
    while 1:
        if index >= len(expression):
            break
        letter = expression[index]
        # letter == 수식 기호일 경우
        if letter == symbol1 or letter == symbol2:
            # 원래부터 괄호가 씌워진 식이 들어오면 그냥 패스
            # ex) (A+B) --> (A+B), ((A+B))가 되면 안됨
            if 2 <= index <= len(expression) - 1:
                if expression[index - 2] == '(' and expression[index + 2] == ')':
                    index += 1
                    continue
            start, end = find_left_right(index)
            # 괄호 안의 괄호가 있을 때 또 괄호를 씌우면 안됨
            # ex) ((A+B)*(C+D)) --> ((A+B)*(C+D)), (((A+B)*(C+D)))가 되면 안됨
            if expression[start - 1] == '(' and expression[end + 1] == ')':
                index += 1
                continue
            # 괄호를 씌울 첫 좌표 ~ 끝 좌표
            start_to_end = expression[start:end + 1]
            # A+B*C-D/E -> A+(B*C)-D/E일 때 B*C가 (B*C)
            expression = expression.replace(start_to_end, put_both(start_to_end))
            index += 1
        index += 1


expression = input().rstrip()
# *와 / 먼저 괄호 씌우고 그 다음 + -
find_symbol_put_both('*', '/')
find_symbol_put_both('+', '-')
while 1:
    tmp = set(expression)
    if '(' not in tmp:
        break
    else:
        expression = open_left_right(expression)

print(expression)
"""
처음 생각
아스키 코드를 활용하면 좋을 것 같다.
문제에서 괄호를 넣어주라고 했는데 복잡할 것 같아서 안 넣고 해보려 했는데 안돼서 일단 괄호를 넣고 다시 생각해보기로...

모르겠다 그냥 너무 많이 고쳐서 당시에 했던 생각을 까먹었다.

풀이
일단 *와 /의 좌우를 괄호로 감싸준 다음, +와 -도 감싸준다.
그리고 큰 괄호부터 하나하나씩 괄호를 제거하면서 후위 표기식으로 바꾸어준다.

문제를 다 풀고 다른 사람 풀이를 보니 내가 너무 복잡하게 푼 거 같다.
그래도 나 혼자 다 푼게 어디야...
"""