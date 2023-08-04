'''
문제 : 카드 (11652)
난이도 : 실버 4

+ 파이썬 정렬 라이브러리의 시간복잡도는 최악의 경우에도 O(NlogN)을 보장

#1
일단 리스트로 입력
set으로 요소 1개씩 남기고
dict와 이용해서 개수 저장

-> 시간초과

#2
마지막에 value가 가장 큰 값 구하는 곳에서 시간초과 일어남
리스트 컴프리헨션을 이용하지 않고 lambda 함수를 이용하면 시간초과가 발생하지 않는다.

+
sorted(nums_dict.items(), key = lambda x:(-x[1],x[0]))
- 정렬의 key(기준이 되는 값)이 (-x[1], x[0])이다. 
- 여기서 x[0]은 딕셔너리의 key, x[1]은 딕셔너리의 value를 의미
- 정렬은 기본적으로 오름차순인데 우리는 value를 기준으로 내림차순으로 정렬해야 하니까 첫 번째 기준이 -x[1]
- 최빈값이 많으면 작은 걸 출력하기 위해 두 번째 기준이 x[0], 즉 x[1]이 같으면 x[0] 순으로 정렬

'''
import sys

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))
nums.sort()

nums_dict = {}
nums_dict[nums[0]] = 1

tmp = nums[0]
for i in range(1, len(nums)):
    if nums[i] != nums[i-1]:
        tmp = nums[i]
        nums_dict[tmp] = 1
    else:
        nums_dict[tmp] += 1

# nums_dict value 기준으로 sort
max_key = sorted(nums_dict.items(), key = lambda x:(-x[1],x[0]))
print(max_key[0][0]) # 빈도 수가 가장 큰 값이 여러 개면 최소값 출력

'''
#1
---------------------------------------
import sys

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))
nums.sort()
nums_dict = dict.fromkeys(list(set(nums)), 0)

nums_dict[nums[0]] += 1

tmp = nums[0]
for i in range(1, len(nums)):
    if nums[i] != nums[i-1]:
        tmp = nums[i]
    nums_dict[tmp] += 1

# nums_dict 중에 value가 가장 큰 key를 리스트로 변환
max_key = [k for k,v in nums_dict.items() if max(nums_dict.values()) == v]
max_key.sort()
print(max_key[0]) # 빈도 수가 가장 큰 값이 여러 개면 최소값 출력
---------------------------------------
'''