import sys
input = sys.stdin.readline

N = int(input())
num_dict = {}
for i in range(N):
    num = int(input())
    num_dict.setdefault(num, 0)
    num_dict[num] += 1

num_list = sorted(num_dict.items(), key=lambda x:x[1], reverse=True)
max_count = num_list[0][1]
tmp = len(num_list) + 1

for i in range(len(num_list)):
    if num_list[i][1] != max_count:
        tmp = i
        break

num_list = sorted(num_list[:tmp])
print(num_list[0][0])

"""
풀이
일단 숫자들을 딕셔너리에 저장해주었다. 그리고 나서 value값이 큰 순서대로 정렬해주었다.
하지만 value가 같다면 더 작은 숫자를 출력해야 하기 때문에 15~18번째 코드로 몇번째까지 value가 같은지 tmp에 인덱스를 저장하고
0번째부터 tmp까지 리스트를 자른다음 key순으로 정렬한다. 그렇게 하면 0번째 리스트에 value가 가장 크면서 key는 가장 작은 숫자가 저장된다. 
"""