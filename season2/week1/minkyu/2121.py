import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())

dot_list = []
for i in range(N):
    dot_list.append(tuple(map(int, input().split())))
dot_set = set(dot_list)
result = 0
for i in range(N):
    x, y = dot_list[i]
    if (x + A, y) in dot_set and (x, y + B) in dot_set and (x + A, y + B) in dot_set:
        result += 1

print(result)

"""
풀이
일단 점들을 리스트에 담아준다.
for 문을 돌면서 그 점에서 사각형이 만들어질 수 있는 점들을 확인한다.
이때 list 에서 확인하지 않고 dot_set 를 만들어 dot_set 에서 확인한다.
 
첫 번째 짠 코드인데 시간 초과가 날 거 같았지만 그래도 일단 짜봤다... 역시 시간 초과가 났다.
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())

dot_list = []
for i in range(N):
    dot_list.append(tuple(map(int, input().split())))

result = 0
for i in range(N):
    if (dot_list[i][0] + A, dot_list[i][1]) in dot_list and (dot_list[i][0], dot_list[i][1] + B) in dot_list and (dot_list[i][0] + A, dot_list[i][1] + B) in dot_list:
        result += 1
print(result)

두 번째 짠 코드도 시간 초과가 날 거 같았지만 그래도 짜봤다.... 또 역시 시간 초과가 났다. 어떻게 시간 줄이지..?
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())

dot_list = []
for i in range(N):
    dot_list.append(tuple(map(int, input().split())))

result = 0
for i in range(N):
    bool_up = False
    bool_right = False
    bool_diagonal = False
    for j in range(i + 1, N):
        if dot_list[i][0] == dot_list[j][0] and dot_list[i][1] + B == dot_list[j][1]:
            bool_up = True
        if dot_list[i][1] == dot_list[j][1] and dot_list[i][0] + A == dot_list[j][0]:
            bool_right = True
        if dot_list[i][0] + A == dot_list[j][0] and dot_list[i][1] + B == dot_list[j][1]:
            bool_diagonal = True
    if bool_up and bool_right and bool_diagonal:
        result += 1

print(result)

세 번째 짠 코드
인터넷에서 파이썬에서 set in 시간복잡도가 O(1)이라는 글을 찾고 set 에서 찾아야 하나 하고 list 가 아닌 set 에서 찾게 했다.
그런데 형변환할때의 시간복잡도를 알고 싶었는데 못 찾아서 list 를 일일히 set(dot_list)로 하고 찾았는데도 시간 초과가 떴다.
혹시 형변환할때 시간이 오래 걸리나 해서 list 를 한 번만 형변환해주고 돌렸더니 맞았다고 됐다.

import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())

dot_list = []
for i in range(N):
    dot_list.append(tuple(map(int, input().split())))
result = 0
for i in range(N):
    x, y = dot_list[i]
    if (x + A, y) in set(dot_list) and (x, y + B) in set(dot_list) and (x + A, y + B) in set(dot_list):
        result += 1

print(result)

이게 왜 해시 문제인지 몰랐는데 파이썬에서 set 가 해시 테이블로 구성되어 있다고 한다.
#https://velog.io/@ready2start/Python-%EC%84%B8%ED%8A%B8set%EC%9D%98-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84 요기 참고
"""