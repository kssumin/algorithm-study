import sys
input = sys.stdin.readline


def check():
    copy_list = num_list[:]
    end = len(copy_list)
    i = 0
    while 1:
        if i >= end - 1:
            break
        if copy_list[i] == ' ':
            copy_list[i - 1] = copy_list[i - 1] * 10 + copy_list[i + 1]
            for j in range(i, end - 2):
                copy_list[j] = copy_list[j + 2]
            end -= 2
            i -= 1
            copy_list.pop()
            copy_list.pop()
        i += 1

    result = copy_list[0]
    for i in range(1, len(copy_list)):
        if copy_list[i] == '+':
            result += copy_list[i+1]
        elif copy_list[i] == '-':
            result -= copy_list[i + 1]
    if result == 0:
        return True
    return False


def BT(index):
    if index >= len(num_list) - 1:
        if check():
            return True
        return False

    for i in range(3):
        if num_list[index] == 'X':
            num_list[index] = symbol[i]
            if BT(index + 2):
                for j in range(len(num_list)):
                    print(num_list[j], end='')
                print()
            num_list[index] = 'X'
    return


N = int(input())

symbol = [' ','+','-']
for _ in range(N):
    num = int(input())
    num_list = list(range(1, num + 1))
    for i in range(1, num):
        num_list.insert(2*i - 1, "X")
    BT(1)
    print()

"""
풀이
백트래킹을 써서 풀었다.
굉장히 풀기 까다로웠다.
일단 식이 완성되면 check 함수를 통해 ''를 없애고 0이 되는지 확인한다.

새롭게 알게된 사실
for문을 쓸 때 만약 for i in range(end)이고 for문 아랫 줄로 코드가 진행됐을 때
i나 end 값을 바꿔줘도 for문 아래에서만 값이 바뀐다. 지역변수 느낌?
"""