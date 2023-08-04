'''
/*문제 정보 */
1912번 - 연속합
난이도 - 실버 2
/*풀이 방법 */
오답 1을 해결하기 위해 인덱스값과 인덱스값 + 이전값 중 최대값을 골라주는
식으로 구했다.
'''
import sys
input = sys.stdin.readline

n = int(input())
list1 = list(map(int, input().split()))

for i in range(1,n):
    list1[i] = max(list1[i] + list1[i-1], list1[i])

print(max(list1))
'''
/*오답 노트*/
오답 1
n = int(input())
list1 = list(map(int, input().split()))

index1 = [0 for i in range(n)]

for i in range(n):
    if list1[i] >= 0:
        index1[i] = 1

count = 0
result = []
for i in range(n):
    if index1[i] == 1:
        count += list1[i]

    else:
        result.append(count)
        count = 0

print(max(result))
처음예제만 보고 단순히 양수면 1 음수면 0으로 해서 1이면 계속 값을 더해주고
0이 나오면 저장 후 초기화 시켜서 그 중 최댓값을 고르는 식으로 생각했었는데,
음수값으로 이어도 최대값이 생기는 경우에는 틀린 값이 나온다.

/*느낀 점*/

'''