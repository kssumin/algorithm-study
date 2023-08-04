import sys
input = sys.stdin.readline

N = int(input())
num_list_N = list((map(int, input().split())))
num_dict_N = {}
for num in num_list_N:
    num_dict_N.setdefault(num, 0)
    num_dict_N[num] += 1

M = int(input())
num_list_M = list((map(int, input().split())))

for number in num_list_M:
    if number in num_dict_N:
        print(num_dict_N[number], end=" ")
    else:
        print("0", end=" ")

"""
풀이
상근이가 갖고 있는 카드를 전부 list 에 넣어준다.
그리고 for 문을 돌면서 dict 에 그 숫자들을 키로 넣어주고 동시에 0으로 초기화하고, 1을 더해준다.
만약 이미 그 숫자가 있으면 0으로 초기화하지 않는다.
출력 할 때에는 딕셔너리에 해당 숫자가 있으면 출력, 없으면 0을 출력한다.


해시를 이용하지 않고 처음 짰던 코드는 시간 초과가 떴다.
input = sys.stdin.readline

N = int(input())
num_list_N = list((map(int, input().split())))

M = int(input())
num_list_M = list((map(int, input().split())))

for number in num_list_M:
    print(num_list_N.count(number), end=" ")


최근에 try except문을 쓴 게 기억 나서 
14~18번째줄을
for number in num_list_M:
    try:
        print(num_dict_N[number], end=" ")
    except:
        print("0", end=" ")
로 했었는데 1116ms로 시간이 더 오래 걸린다.
"""
