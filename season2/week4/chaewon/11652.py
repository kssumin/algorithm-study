# BJ 11652 : 카드 / SILVER IV / 144ms

import sys

n = int(sys.stdin.readline().strip())

nums = list(map(int, list(sys.stdin.readline().strip() for _ in range(n))))

# key: nums, value: 0인 딕셔너리 생성
nums_cnt = dict.fromkeys(nums, 0)

# nums 안을 돌면서 num이 나오면 nums_cnt[i]에 1씩 더해줌
for num in nums:
    nums_cnt[num] += 1

# 가장 많은 빈도수값을 저장
max_cnt = max(nums_cnt.values())

# max_cnt를 value로 가지고 있는 key값들을 모두 results list에 저장
results = [k for k, v in nums_cnt.items() if v == max_cnt]

# results의 최솟값을 출력함으로써, 최빈값이 여러 개일때 작은 것을 출력하는 조건을 성립시킴
print(min(results))


'''
NOTE:

어렵지 않게 풀었어요!! 굿
'''