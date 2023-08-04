'''
문제 : 두 용액 (2470)
난이도 : 골드 5

용액들 중 2개를 선택해서 0에 가깝게 만들어야 하는 문제

#1
투 포인터로 절댓값이 큰 쪽을 줄여보자..!
투 포인터 사용, nums는 정렬된 상태여야 함
각각 시작은 처음과 끝 -> i, j
nums[i]와 nums[j] 중 절댓값이 큰 쪽을 줄이기
- nums[i]가 절댓값이 크면 i++
- nums[j]가 절댓값이 크면 j--

'''
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()     # 입력받은 리스트 정렬

i, j = 0, n - 1     # 각 포인터의 시작
answer = [nums[i], nums[j]]

while i < j:
    if abs(nums[i] + nums[j]) < abs(sum(answer)):
        answer = [nums[i], nums[j]]

    # 절댓값 크기 비교해서 포인터 이동
    if abs(nums[i]) <= abs(nums[j]):
        j -= 1
    else:
        i += 1

print(answer[0], answer[1])