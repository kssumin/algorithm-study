'''
/*문제 정보 */
2961번 - 도영이가 만든 맛있는 음식
난이도 - 실버 2
/*풀이 방법 */
조합을 이용해 쓴맛과 신맛의 차이값을 구해 계속 최솟값 갱신해준다.

'''
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split(" "))) for _ in range(n)]
comb = [combinations(arr, i) for i in range(1, n+1)]

result = sys.maxsize


for com in comb:
    for a in com:
        sour, bitter = 1, 0
        for s, b in a:
            sour *= s
            bitter += b
        result = min(result, abs(sour-bitter))
print(result)
'''
/*오답 노트*/
풀이 1
import sys
input = sys.stdin.readline

n = int(input())

sour = []    # 신 맛
bitter = []  # 쓴 맛

for i in range(n):
    s, b = map(int, input().split())
    sour.append(s)
    bitter.append(b)

s_count = 1
b_count = 0
result = abs(sour[0] - bitter[0])

for i in range(n):
    s_count *= sour[i]
    b_count += bitter[i]
    result = min(result, abs(s_count - b_count))

print(result)

이 풀이는 재료를 선택적으로 빼지 못한다. 사실 조합 써야된다고 알고 있으면서도
조합을 써본적이 없어서 썼던 풀이....

매우 이해가 안가는 상황
for com in comb:
    for a in com:
        sour, bitter = 1, 0
이 지금 정답 풀이 인데
sour, bitter = 1, 0
for com in comb:
    for a in com:
로 놓으면 오답 처리 돼요.... 개인적으로 이해가 안가요 왜그런지..        
/*느낀 점*/
조합 문제를 여러번 풀어도 나중에 나와도 쉽게 사용할 수 있게 해야 겠다.
'''
