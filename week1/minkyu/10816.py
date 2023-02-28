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
