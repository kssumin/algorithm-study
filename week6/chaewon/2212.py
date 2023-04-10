# BJ 2212 : 센서 / GOLD V / 48ms

import sys

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())

# n개의 센서에 대한 좌표를 리스트로 저장 후 오름차순 정렬
n_coor = list(map(int, sys.stdin.readline().strip().split()))
n_coor.sort()

# n_coor[i+1] - n_coor[i]의 값을 area_max에 저장한 후 오름차순 정렬
# 즉, n_coor에 저장된 센서들 중 "이웃한 센서 간 거리"를 모두 저장한 후 정렬
area_max = []
for i in range(n-1):
    area_max.append(n_coor[i+1] - n_coor[i])
area_max.sort()


# k가 1이 아닐 때
if k != 1:
    # 센서들 중에 가장 멀리 떨어져 있는 센서 두 개의 좌표 차이
    diff_mn = max(n_coor) - min(n_coor)

    # a는 area_max 중, 가장 큰 애들 k-1개를 뽑아서 더해줌
    # a = diff_mn - "각 집중국의 수신 가능영역의 거리의 합"
    a = sum(area_max[-(k-1):])
    result = diff_mn - a

# k가 1일 때는 diff_mn이 답임
# 집중국 1개로 모든 센서를 연결해야 하므로
else:
    result = max(n_coor)-min(n_coor)

print(result)



'''
NOTE:

문제는 어떻게 이해를 했는데..
예제 2번이 이해가 안돼서 질문게시판을 찾아봤다.
문제를 이해하기 쉽게 설명한 글이 있어서 그 글을 참고하여 직접 그림을 그려보면서 규칙을 찾았다.
-------

핵심 아이디어 : 

집중국이 K개 -> 연결되지 않은? 구역이 K-1개
              이 구간 길이 합이 최대가 되게 하면 됨

n_coor = [x_0, x_1, x_2, ..., x_n]

k-1 개 원소로 이루어진 i 집합에 대하여,
sum( x_i - x_(i-1) )가 최대여야 함
-------

처음에는 k가 1일 때 / 1이 아닐 때 조건을 안 나눠줘서 오답 처리가 되었다ㅠㅠ

반례를 생각해봤다.
k = 1일 때,
a = sum(area_max[-(k-1):]) = sum(area_max[-0:]) = sum(area_max) 가 된다.
즉, area_max 전체 원소의 합이 a가 된다.
그래서 조건문으로 구분해주고 k = 1일 때 diff_max를 반환해주게끔 했다.
-------

혼자 힘으로 풀어서 넘 기뻐용
변수명 정하는 것도 정말 어려운 것 같다... a를 다른 이름으로 바꾸고 싶었는데 표현하기가 어려웠다
다음엔 변수이름도 잘 정해봐야징

'''