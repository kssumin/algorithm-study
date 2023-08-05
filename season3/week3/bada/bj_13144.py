'''
문제 : List of Unique Numbers
난이도 : 골드4

시간 초과가 떠서 답을 봤다아...

이 문제는 투포인터를 이용해야 한다.

종료 조건은 start와 end가 모두 마지막 원소를 가리킬 때
'''
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))


result = 0
start, end = 0, 0
# 수열에 들어갈 수 있는 최댓값인 100000 크기의 배열을 만들고, 숫자가 중복되었는지 체크
seq = [False for _ in range(1000001)]
while start < n and end < n:
    if not seq[nums[end]]:      # start부터 end까지 중복 숫자 없으면
        seq[nums[end]] = True
        end += 1
        result += (end - start)     # end를 포함하여 만들 수 있는 수열의 개수
    else:
        seq[nums[start]] = False
        start += 1

print(result)
