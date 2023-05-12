import sys
input = sys.stdin.readline

N = int(input())
num_set = set(map(int, input().split()))
M = int(input())
input_list = list(map(int, input().split()))
for num in input_list:
    if num in num_set:
        print(1, end=" ")
    else:
        print(0, end=" ")


"""
주제는 이분탐색이지만 set로 푸는게 더 빠르고 쉬울 거 같아서 이렇게 풀었다.
"""