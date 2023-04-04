'''
문제 : 로프
난이도 : 실버4

N개의 로프로 들어올릴 수 있는 물체의 최대 중량을 구하자
각 로프가 들어올릴 수 있는 중량은 다르고, 병렬로 연결해서 분산할 수 있다.

#1
- 입력받은 값들을 배열로 만들고 정렬한다. 

설명을 잘 못 하겠어서 예시를 설명해보겠습니다!!!

입력값 : [4, 17, 9]
1. 정렬
[4, 17, 9] -> [4, 9, 17]

2. 가능한 모든 경우의 수는?
i) 4, 9, 17 사용
-> 4 + 4 + 4 = 12

4, 9 사용과 4, 17 사용은 고려할 필요 없음 / Why? 당연히 i)보다 최대 중량이 작으니까

ii) 9, 17 사용
-> 9 + 9 = 18

iii) 17 사용
-> 17

정답 : 18

3. 결국 정렬한 값을 순회
index i에 value가 v인 경우 v * (n - i)을 최댓값과 비교해서 더 큰 값이 answer!
'''
import sys

n = int(sys.stdin.readline())

weights = []
for _ in range(n):
    weights.append(int(input()))
weights.sort()

answer = 0
for i in range(n):
    answer = max(answer, weights[i] * (n - i))

print(answer)
