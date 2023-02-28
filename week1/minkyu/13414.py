import sys
input = sys.stdin.readline

K, L = map(int, input().split())

class_order = dict()
for i in range(1, L + 1):
    school_num = input().rstrip()
    class_order[school_num] = i
class_order = sorted(class_order.items(), key=lambda x: x[1])

result = 0
for num in class_order:
    if result == K:
        break
    print(num[0])
    result += 1

"""
처음에 짰던 코드는 시간 초과가 떴다.
input = sys.stdin.readline

K, L = map(int, input().split())

student_list = []
for i in range(L):
    school_num = int(input())
    if school_num in student_list:
        student_list.remove(school_num)
        student_list.append(school_num)

    else:
        student_list.append(school_num)

for i in range(K):
    print(student_list[i])

두 번째 짰던 코드도 시간 초과가 떴다.
key value 값을 서로 바꿔주는게 for 문으로 하나씩 돌면서 시간이 오래 걸리는 것 같다.
input = sys.stdin.readline

K, L = map(int, input().split())

class_order = dict()
for i in range(1, L + 1):
    school_num = input().rstrip()
    if school_num in class_order:
        del class_order[school_num]
        class_order[school_num] = i
    else:
        class_order[school_num] = i
class_order = {v:k for k,v in class_order.items()}
result = 0
tmp = 1

while 1:
    if tmp in class_order:
        print(class_order[tmp])
        result += 1
    tmp += 1
    if result == K:
        break
        
무의식적으로 숫자니깐 int(input)을 했다. 계산을 안해도 되는 숫자인데 int(input)을 하면 안됐다.
int 형변환을 해버리면 학번 맨 앞에 0이 들어갈 때 0을 없애버린다.... 문제 조건을 자세히 봐야겠다..

그냥 input()했더니 또 틀렸다.
sys 로 받을 때는 rstrip 을 해주자... 개행문자가 같이 들어간다.  
"""