import sys
input = sys.stdin.readline


def swap(str1, op, str2):
    return str1+str2+op


def put_both(string):
    return '(' + string + ')'


def find_left_right(index):
    if expression[index - 1] == ')' and expression[index + 1] == '(':
        tmp_index = index
        stack = []
        while 1:
            tmp_index -= 1
            if expression[tmp_index] == ')':
                stack.append(')')
            elif expression[tmp_index] == '(':
                stack.pop()
                if not stack:
                    st = tmp_index
                    break
        tmp_index = index
        stack = []
        while 1:
            tmp_index += 1
            if expression[tmp_index] == '(':
                stack.append('(')
            elif expression[tmp_index] == ')':
                stack.pop()
                if not stack:
                    ed = tmp_index
                    break
        return st, ed
    # *나 /기호 왼쪽에 ()가 있음
    elif expression[index - 1] == ')':
        tmp_index = index
        stack = []
        while 1:
            tmp_index -= 1
            if expression[tmp_index] == ')':
                stack.append(')')
            elif expression[tmp_index] == '(':
                stack.pop()
                if not stack:
                    break
        return tmp_index, index + 1
    # *나 /기호 오른쪽에 ()가 있음
    elif expression[index + 1] == '(':
        tmp_index = index
        stack = []
        while 1:
            tmp_index += 1
            if expression[tmp_index] == '(':
                stack.append('(')
            elif expression[tmp_index] == ')':
                stack.pop()
                if not stack:
                    break
        return index - 1, tmp_index
    # *나 /기호 양 옆에 ()가 없음
    else:
        return index - 1, index + 1


def open_left_right(string):
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
            return string.replace(string[start-1:end+2], swap(string[start:i], expression[i], string[i+1:end+1]))

    return string[1:len(string)-1]
expression = input().rstrip()
result = expression
"""
for i in range(len(expression)):
    letter = expression[i]
    if letter == '*' or letter == '/':
        start, end = find_left_right(i)
        start_to_end = expression[start:end + 1]
        result = result.replace(start_to_end, put_both(start_to_end))
expression = result
for i in range(len(expression)):
    letter = expression[i]
    if letter == '+' or letter == '-':
        start, end = find_left_right(i)
        start_to_end = expression[start:end + 1]
        result = result.replace(start_to_end, put_both(start_to_end))
"""
index = 0
a = expression
while 1:
    if index >= len(expression):
        break
    letter = expression[index]
    if letter == '*' or letter == '/':
        if 2 <= index <= len(expression) - 1:
            if expression[index - 2] == '(' and expression[index + 2] == ')':
                index += 1
                continue
        start, end = find_left_right(index)
        if expression[start-1] == '(' and expression[end+1] == ')':
            index += 1
            continue
        start_to_end = expression[start:end + 1]
        expression = expression.replace(start_to_end, put_both(start_to_end))
        index += 1
    index += 1
index = 0
while 1:
    if index >= len(expression):
        break
    letter = expression[index]
    if letter == '+' or letter == '-':
        if 2 <= index <= len(expression) - 1:
            if expression[index - 2] == '(' and expression[index + 2] == ')':
                index += 1
                continue
        start, end = find_left_right(index)
        if expression[start-1] == '(' and expression[end+1] == ')':
            index += 1
            continue
        start_to_end = expression[start:end + 1]
        expression = expression.replace(start_to_end, put_both(start_to_end))
        index += 1
    index += 1
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
*와 /가 나왔을 때 괄호로 먼저 감싸주어야 하기 때문에 *와 /가 중요해보인다.
문제에서 괄호를 넣어주라고 했는데 복잡할 것 같아서 안 넣고 해보려 했는데 안돼서 괄호를 넣고 다시 생각해보기로...

코드가 너무 길고 설명도 별로 없는데 일단 겨우 다 풀어서 제출했는데 깔끔하게 정리해서 나중에 다시 올릴게용
"""