'''
/*문제 정보 */
3079번 - 입국심사
난이도 - 골드 5
/*풀이 방법 */
소요되는 시간에 대해 이분탐색으로 풀었다.
start = 0, end = 최장 시간 * 인원 수로 해야 했다.
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sim = []

for _ in range(n):
    sim.append(int(input()))

start = 0
end = max(sim) * m
answer = 0

while start <= end:
    mid = (start + end) // 2

    count = 0
    for time in sim:
        count += mid // time
        if count > m:
            break

    if count < m:
        start = mid + 1

    else:
        end = mid - 1
        answer = mid

print(answer)

'''
/*오답 노트*/
/*느낀 점*/
이분탐색은 비슷한 코드에서 어떤 것을 변수로 설정하는지 찾는 문제인 것 
같다. 너무 어렵다...
'''