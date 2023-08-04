import sys
input = sys.stdin.readline
INF = sys.maxsize

sentence = input().rstrip()
# 아래 코드 작성 안하면 마지막 숫자를 더하거나 뺴지 않음
sentence += '+'
tmp = ""
plus = 0
minus = 0
index = INF
for i in range(len(sentence)):
    if sentence[i] == '-':
        index = i
        break

for i in range(len(sentence)):
    letter = sentence[i]
    if letter == ')' or letter == '(':
        continue
    else:
        # letter가 숫자
        if letter.isdigit():
            tmp += letter
        # letter가 기호
        else:
            if i > index:
                minus += int(tmp)
            else:
                plus += int(tmp)
            tmp = ""
print(plus - minus)

"""
풀이
이 문제는 괄호를 제거하는 것, 문자열로 된 숫자를 숫자로 구분하는 것, -기호 뒤에 숫자는 전부 빼야되는 것 세 가지가 중요하다.
인줄 알았는데 이미 입력에서 괄호를 제거했었네용...?
문자열로 된 숫자는 tmp를 이용해서 for문을 돌 때 숫자면 tmp에 추가하고, 기호가 오면 tmp를 숫자로 인식했다.
처음 for문을 돌 때 -의 기호의 인덱스를 index에 저장하고 for문을 돌면서 숫자로 인식 될 때의 인덱스가 index 보다 작다면 plus에,
아니라면 minus에 더해주었다. 
"""
