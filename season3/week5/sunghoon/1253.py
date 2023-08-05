'''
/*문제 정보 */
1253번 - 좋다
난이도 - 골드4
/*풀이 방법 */
https://velog.io/@prairie_sky/%EB%B0%B1%EC%A4%80-1253-%EC%A2%8B%EB%8B%A4-Python
직접 작성한 코드가 예제는 올바르게 나오지만 계속 런타임 에러가 떠
코드 리뷰 했습니다.
투포인터로 타겟 값을 정하고 그 타겟값을 제외한 배열에서 투포인터를
이용해 탐색을 진행하였다.
'''
# 좋은 수의 개수를 세는 함수
def solve():
    cnt = 0
    nums.sort()
    for i in range(len(nums)):
        if search(i, nums[i]):
            cnt += 1
    print(cnt)


# 좋은 수가 들어있는지 탐색하는 함수
def search(i, target):
    temp = nums[:i] + nums[i+1:]  # 타겟이 되는 nums[i]를 제외하고 탐색
    # print(temp)
    left = 0
    right = n-2  # 마지막 인덱스 n-1에서 타겟값 하나 더 빼서 n-2
    while left < right:
        sum = temp[left] + temp[right]
        if target < sum:
            right -= 1
        elif target > sum:
            left += 1
        else:
            # print(i,target)
            return True
    return False


import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
solve()
'''
/*오답 노트*/
오답 노트 1. 종이가 없어서 그냥 머릿속으로 했는데 반복문에 갇혔따...
import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
li.sort()

count = 0

first = 0
end = n
for i in range(n):
    first = i
    end -= 1
    while first <= end:
        if li[first] + li[end] in li:
            count += 1
            first += 1

print(count)

오답 2. 
 elif li[first] + li[end] > goal:
            end -= 1
        else:
            start +=1
/*느낀 점*/
투포인터가 다른 문제에 비해 쉽다고 생각해 그냥 부딪혔는데 런타임
에러 늪에 빠졌다. 이 블로그 코드에서 리뷰를 했는데, 정말 지식을 얻어가는
느낌이었다. 내가 본 블로그 글 중에 가장 설명이 이해하기 쉽게 설명
되어있고, 코드 구조도 얻어가는게 많은 것 같다.
'''