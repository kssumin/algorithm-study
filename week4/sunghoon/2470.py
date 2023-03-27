'''
/*문제 정보 */
2470번 - 두 용액
난이도 - 골드 5
/*풀이 방법 */
투포인터를 이용해 두 용액을 섞고 0과 가장 가까운 값을
abs 절대값을 이용해 기준값을 계속 갱신하고 기준값을 만든 용액을 저장해서 출력
'''
import sys
input = sys.stdin.readline

n = int(input())

water = list(map(int, input().split()))      # 용액 리스트 받아주기
water = sorted(water)

left, right = 0, n - 1         # 투포인터

a = sys.maxsize   # 그냥 비교값
result = []   # 출력값

#  전문제를 통해 익힌 투포인터
while left < right:
    sum1 = water[left] + water[right]

    if abs(sum1) < a:
        a = abs(sum1)
        result = [water[left], water[right]]

    if sum1 < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])
'''
/*오답 노트*/
/*느낀 점*/
1. "0과 가장 가까운 값"에서 많이 헤맸었다. abs 절대값 함수를 알게 되고
   코드를 작성했다. abs 와 투포인터를 알면 풀 수 있었다.!

2. 처음에 기준값을 10으로 잡아놨다가 런타임에러가 나와서 10억을 해도 런타임에러가 
   나왔다. 반례를 계속 생각하다가 용액리스트가 최대값으로만 되어 있다면 20억이 정답이
   되기 때문에 20억1 로 기준값을 해놔야 정답이 되었다. 그냥 앞으로 sys.maxsize 이용
   해야겠다...
'''