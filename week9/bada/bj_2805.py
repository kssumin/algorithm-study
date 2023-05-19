'''
문제 : 나무 자르기
난이도 : 실버2

나무의 수(n)와 집으로 가져가려고 하는 나무의 길이(m)가 주어짐.
적어도 m미커의 나무를 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값 구하기
'''
import sys

n, m = map(int, sys.stdin.readline().split())
tree = sorted(list(map(int, sys.stdin.readline().split())))

start = 1
end = max(tree)

while start <= end:
    mid = (start + end) // 2
    count = 0

    for t in tree:
        if t > mid:
            count += t - mid

    if count >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
