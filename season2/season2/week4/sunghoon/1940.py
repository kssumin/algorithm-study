'''
/*문제 정보 */
1940번 - 주몽
난이도 - 실버 4
/*풀이 방법 */
리스트를 정렬해주고 투포인터를 이용해 준다.
'''
import sys
input = sys.stdin.readline

n = int(input())     # 재료 개수 n
m = int(input())     # 고유 번호 m
l = list(map(int, input().split()))  # 재료 번호를 l에 저장

l.sort()
count = 0            # 만든 횟수 저장
left, right = 0, len(l) - 1        # 투포인터

while left < right:
    total = l[left] + l[right]
    if total > m:       # 토탈 값이 m 보다 크니까 오른쪽 값을 내려준다.
        right -= 1
    elif total < m:     # 토탈 값이 m 보다 작으니까 왼쪽 값을 올려준다.
        left += 1

    else:               # 값을 찾았으니 양쪽에서 조여준다.
        count += 1
        left += 1
        right -= 1

print(count)


'''
/*오답 노트*/
/*느낀 점*/
1. 처음에 l = input().split()이라고 적어서 런타임 에러가 났다. 처음에 list()까지 적어
   줬었는데, 안에 값들을 int로 받아 주는 것까지 생각을 했어야 했다.
2. 크게 중요한건 아니지만 split()을 쓰면 리스트로 저장된다는 것도 알게 되었다.
3. 처음에는 난이도도 쉽고 주제도 상대적으로 가벼운 것 같아서 막 풀다가
   이렇게 푸는게 아니란걸 직감하자마자 찾아보니 "투포인터"라는 것을 알게 되었다.
'''