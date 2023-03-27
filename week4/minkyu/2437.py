import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
weights = list(map(int, input().split()))
weights.sort()
weights.append(INF)
result = 0
if weights[0] != 1:
    print(1)
    weights = []
num = 1
max_num = 1
for i in range(1, len(weights)):
    if max_num + 1 >= weights[i]:
        max_num += weights[i]
    else:
        print(max_num + 1)
        break



"""
풀이
일단 0번째 숫자가 1이 아니면 1을 출력한다. 0번째 숫자가 1이면 만들 수 있는 최대의 숫자(max_num)를 1로 한다.
그 다음 i=1부터 max_num + 1과 weights[i]를 비교한다.
만약 max_num + 1이 weights[i]보다 작다면 max_num + 1 숫자를 만들 수 없다.
따라서 max_num + 1을 출력한다.
 - max_num이 15라면 1~15의 숫자는 다 만들 수 있어서 위의 식이 가능하다.
첫번째 코드
제일 쉬워보이는 방법을 썼다.
입력 받은 숫자들을 다 더해서 나올 수 있는 경우의 수를 전부 구했다.
메모리 초과가 떴다.
import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
weights = list(map(int, input().split()))
result = []
result_set = set()

for i in range(1, N + 1):
    tmp = list(combinations(weights, i))
    for j in range(len(tmp)):
        result_set.add(sum(tmp[j]))

num = 1
while 1:
    if num not in result_set:
        break
    num += 1

print(num)
두번째 코드
와 진짜 시간 줄일대로 줄였는데도 시간초과가 난다.
num이 1부터 1씩 증가하면서 입력받은 값에 있는지 보고 없으면 num과 가장 가깝지만 num보다는 작은 수의 인덱스를 구한다.
num에서 인덱스를 줄여가며 뺄 수 있는지 보고 빼준다. 만약 0이 되면 다음 수로 넘어가고
0이 되지 않는다면 그 수를 만들 수 없다는 뜻이니 그 수를 출력한다.  
너무 일차원적으로 풀어서 그런 것 같다. 다른 방법이 생각나서 그걸로 해봐야겠다.
import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
weights = list(map(int, input().split()))
weights.sort()
weights.append(INF)
weights_dict = {}
for i in range(len(weights)):
    weights_dict.setdefault(weights[i], 0)
    weights_dict[weights[i]] += 1

num = 1
index = 0
while 1:
    tmp_list = []
    if num not in weights_dict:
        # num 숫자보다 처음으로 커진 숫자의 인덱스 찾기
        while 1:
            if weights[index] > num:
                break
            else:
                index += 1
        tmp = num
        for i in range(index - 1, -1, -1):
            if tmp - weights[i] >= 0:
                tmp -= weights[i]
                weights_dict[weights[i]] -= 1
                tmp_list.append(weights[i])
            if tmp in weights_dict and weights_dict[tmp] > 0:
                tmp = 0
                break
        for i in range(len(tmp_list)):
            weights_dict[tmp_list[i]] += 1
        if tmp != 0:
            print(num)
            break

    num += 1
"""