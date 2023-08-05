N = int(input())
nums = list(map(int, input().split()))
nums.sort()

count = 0

for i in range(N):
    eraseArr = nums[:i] + nums[i+1:]
    left = 0
    right = len(eraseArr) - 1
    while left < right:
        if eraseArr[left] + eraseArr[right] == nums[i]:
            count += 1
            break
        elif eraseArr[left] + eraseArr[right] < nums[i]:
            left += 1
        else:
            right -= 1

print(count)