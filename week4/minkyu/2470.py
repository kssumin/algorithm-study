import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

left = 0
right = N - 1

answer = INF
result = []

while left < right:
    num_left = num_list[left]
    num_right = num_list[right]

    num = num_left + num_right
    if abs(num) < answer:
        answer = abs(num)
        result = [num_left, num_right]

    if num < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])

"""
풀이
리스트의 처음과 끝에서 하나씩 인덱스를 줄여가면서 0이 되는지 확인한다.

처음 생각
1. 입력값의 절댓값에 로그를 씌워서 리스트를 분류해서 끼리끼리 수를 비교해야하나?
2. 그냥 +와 -로 분류해서 정렬해서 수를 비교하는게 나을 것 같다
3. +와 -가 섞여서 들어오면 잘 될 거 같은데 +만 들어오거나 -만 들어오면 안돼서 이분탐색으로 해봄
4. 구글링...
 
첫번째 코드
전부 탐색해야해서 당연히 시간 초과가 날 거 같았지만 해봤다.
for num in num_list:
    if num > 0:
        plus_list.append(num)
    else:
        minus_list.append(num)

plus_list.sort()
minus_list.sort(reverse=True)

for n1 in plus_list:
    tmp = INF
    for n2 in minus_list:
        if tmp > abs(n1 + n2):
            tmp = n1 + n2
            result = (n1, n2)

두 번째 코드
이것도 시간 초과가 날 것 같았는데 이건 메모리 초과가 났다.
for num in num_list:
    if num > 0:
        plus_list.append(num)
    else:
        minus_list.append(num)

plus_list.sort()
minus_list.sort(reverse=True)
result = []
for n1 in plus_list:
    tmp = INF
    for n2 in minus_list:
        if tmp > abs(n1 + n2):
            tmp = n1 + n2
            result.append((tmp, n1, n2))
        else:
            break
result.sort()
print(result[0][1], result[0][2])
세 번째 코드
이진 탐색으로 입력값에 -1을 곱한 값을 찾아서 해당 값이 있으면 그 숫자를 출력하고, 없으면 그 숫자에 가까운 숫자를 출력하게 했다.
거의 다 했는데 같은 숫자를 출력하게 하는 경우가 있어서 포기했다. ex) -98 -97 1 일 때 1 1을 출력함...
같은 숫자가 나올 때 if 문으로 다시 비교하면 되긴하는데 그러면 코드가 너무 복잡해질 거 같아서 그냥 답을 봤다...
사실 아래 코드는 0 뺴고는 잘 작동하는데 입력으로 0 들어왔을 때 또 if 문 쓰기 싫었다. 너무 땜빵용 코드 같아서

def binary_search(num_list, num):
    start, end = 0, len(num_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if num == num_list[mid]:
            return num_list[mid]
        if num > num_list[mid]:
            start = mid + 1
        else:
            end = mid - 1

    if start == len(num_list):
        return num_list[-1]
    elif end == -1:
        return num_list[0]
    else:
        if -num == num_list[start] and start + 1 < len(num_list):
            start += 1
        else:
            start = end
        if abs(num_list[start] - num) > abs(num_list[end] - num):
            return num_list[end]
        else:
            return num_list[start]
"""

