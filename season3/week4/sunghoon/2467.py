'''
/*문제 정보 */
2467번 - 용액
난이도 - 골드 5
/*풀이 방법 */
투포인터로 정렬된 용액리스트에서 비교값에 따라 포인터를 이동시켜 정답을 구했따.

'''
import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

left = 0
right = n-1

sum1 = abs(s[left] + s[right])
result1, result2 = left, right

while left < right:
    mixed = s[left] + s[right]

    if abs(mixed) < sum1:
        sum1 = abs(s[left] + s[right])
        result1, result2 = left, right

        if sum1 == 0:
            break

    if mixed < 0:
        left += 1

    else:
        right -= 1

print(s[result1], s[result2])
'''
/*오답 노트*/
저번에 풀어본 적이 있어 따로 노트에 적어가며 하지 않고, 변수명도
가독성 있이 하지 않아서 각종 런타임 에러와 오류, 오답이 나왔다...
/*느낀 점*/
매번 while 반복문 조건을 그냥 while 1: 로 설정 해놓는데
투포인터는 left < right 인 것을 생각해두자.
'''