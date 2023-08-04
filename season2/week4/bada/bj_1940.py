'''
문제 : 주몽 (1940)
난이도 : 실버 4

# 1
합해서 M이 되는 두 숫자의 쌍의 개수를 찾아라!
키워드가 정렬..

- 입력받은 번호 리스트를 저장해서 오름차순으로 정렬하고, 중앙값을 기준으로 2개의 리스트로 분리
- small 리스트를 순회하면서 big 리스트에 원하는 값이 있는지 찾기
- 원하는 값이 있는지 찾기 위해서 big 리스트를 순회하며 만약 현재 값이 원하는 값보다 작으면 break -> 없음

이런 식으로 해보자! 

# 2
중앙값을 기준으로 나누는 게 아니라 m // 2 보다 큰 값과 작은 값으로 나눠야 함!

-> 정답!
'''
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
small, big = [], []

# m // 2 값을 기준으로 리스트 나누기
for i in nums:
    std = m // 2
    if i > std:
        big.append(i)
    else:
        small.append(i)

count = 0
for s in small:
    target = m - s
    for j in range(len(big)):
        tmp = big[j]
        if tmp < target:
            continue
        elif tmp == target:
            count += 1
            big.pop(j)
            break
        else:   # tmp가 target 보다 크면 뒤에 있는 값도 target보다 크기 때문에 break
            break

print(count)