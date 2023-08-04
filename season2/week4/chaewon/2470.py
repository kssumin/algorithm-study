# BJ 2470 : 두 용액 / GOLD V / 148ms

import sys

n = int(sys.stdin.readline().strip())
liquid = list(map(int, sys.stdin.readline().strip().split()))
liquid.sort()

left = 0
right = n - 1

answer = abs(liquid[left] + liquid[right])
result = [liquid[left], liquid[right]]


while left < right:
    left_feature = liquid[left]
    right_feature = liquid[right]

    mixture_feature = left_feature + right_feature

    # 현재 위치에서 만든 혼합물의 특성 값의 절댓값이, answer보다 작으면
    if abs(mixture_feature) < answer:

        # answer를 그 특성값으로 바꿔 주고
        answer = abs(mixture_feature)

        # 최종 답이 될 result 값에 이 혼합물을 이루는 액체들을 저장
        result = [left_feature, right_feature]

        # 만약 answer, 즉 현재 혼합물 값이 0이면 while문을 종료함 -> result를 바로 출력할 수 있게
        if answer == 0:
            break

    # 현재 위치에서 만든 혼합물의 특성 값이 음수이면
    if mixture_feature < 0:

        # left 값을 1씩 더해줌으로써, left_feature값이 점점 커지게 해줌 -> 혼합물 값이 커짐
        left += 1

    # 현재 위치에서 만든 혼합물의 특성 값이 양수이면
    else:

        # right 값을 1씩 빼줌으로써, right_feature값이 점점 작아지게 해줌 -> 혼합물 값이 작아짐
        right -= 1



print(result[0], result[1])


'''
NOTE:

입력받은 특성에서 두 개를 어떻게 뽑아야하는지 몰라서 헤맸다ㅠ
이중for문을 사용했는데, 그렇게 하니까 시간 초과가 났다. 당연한 게 O(n^2)인데 n이 최대 100,000이라...
원인을 알고 있는데도 해결할 수 있는 아이디어가 떠오르지 않았다

그래서 결국 코드를 찾아봤다!

핵심 아이디어: 절댓값이 비슷한 음수와 양수를 합쳐야 0과 가까운 수가 나오므로, 배열을 정렬한 후 양쪽 끝에서부터 비교해나간다

코드를 한 줄씩 따라 적으면서 이해해봤다.

처음엔 result에 왜 초기값을 넣는 건지 이해가 안돼서 그냥 [0, 0]을 넣었는데 오답처리 됐다.
생각해보니, 만약 초기값, 즉 양 끝에 있는 값을 더한 값이 가장 0과 가깝다면, result 내의 값은 변하지 않고
초기값이 그대로 출력되는 구조였다.

수정을 하니 정답 처리가 됐다!

'''

'''
# 처음 작성한 시간 초과 코드
# BJ 2470 : 두 용액 / GOLD V /
import random
import sys


n = int(sys.stdin.readline().strip())
liquid = list(map(int, sys.stdin.readline().strip().split()))
result = dict()

for i in range(0, n):
    for j in range(i+1, n):
        feature_sum = abs(liquid[i] + liquid[j])
        
        # key: 두 용액의 특성값, value: 합의 절댓값 을 딕셔너리 형태로 저장
        result[(liquid[i], liquid[j])] = feature_sum

        # 저장한 값이 result에 저장된 feature_sum의 최솟값보다 크면, 필요없는 값이므로 다시 삭제해준다
        if result and feature_sum > min(result.values()):
            del result[(liquid[i], liquid[j])]

# 리스트 내를 모두 다 돌고 나와 최솟값을 찾고
min_sum = min(result.values())

# 그 최솟값을 value로 가지고 있는 key를 min_list에 저장한다
min_list = [k for k, v in result.items() if v == min_sum]

# 그 중 랜덤으로 한 개 추출한 값을 answer로 받아온다
answer = sorted(random.sample(min_list, 1)[0])

print(' '.join(map(str, answer)))
'''