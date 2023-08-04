'''
문제 : 크게 만들기
난이도 : 골드3

n자리 숫자가 주어졌을 때, 여기서 숫자 k개를 지워서 얻을 수 있는 가장 큰 수


#1
앞에서 k개 숫자에서 가장 큰 자리수의 값이 되는 숫자를 찾고
그 숫자 뒤의 숫자들 중에서 크기가 작은 값들 제거

모르겠어요.....

#2 코드 리뷰
numbers에 있는 숫자를 하나씩 stack에 넣고 그 다음 숫자와 비교
다음 숫자가 stack에 있는 숫자보다 크면 stack.pop()을 해주면서 가장 큰 숫자를 앞 쪽에 위치
k개까지만 지우기
만약 k개 미만으로 숫자를 지웟으면 뒤에 있는 숫자를 남은 k개 만큼 지우고 출력
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

numbers = input().rstrip()
stack = []
for number in numbers:
    while stack and stack[-1] < number and k > 0:
        stack.pop()
        k -= 1
    stack.append(number)
if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))


'''
import sys

n, k = map(int, sys.stdin.readline().split())
num = list(sys.stdin.readline().strip())
num_list = list(enumerate(num))

count, first, max_value = 0, 0, 0

for i in range(k):
    n = num_list[i]
    if (max_value < int(n[1])):
        max_value = int(n[1])
        first = n[0]
num = num[first:]
max_value = max_value[first:]
k -= first

min_value = 10
for i in range(k):
    n = num_list[i]
    if (min_value > int(n[1])):
        min_value = int(n[1])

'''
