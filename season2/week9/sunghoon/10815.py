'''
/*문제 정보 */
10815번 - 숫자 카드
난이도 - 실버 5e
/*풀이 방법 */
이분탐색이 더 어려워 보여 상근이가 가진 카드값을 딕셔너리에 저장하고
비교값이 딕셔너리에 없으면 0, 있으면 1로 표기했다.
'''
import sys
input = sys.stdin.readline

n = int(input())
sang = list(map(int, input().split()))
m = int(input())
cards = list(map(int, input().split()))

dic = {}
for i in range(len(sang)):
    dic[sang[i]] = 1

for j in range(m):
    if cards[j] in dic:
        print(1, end=' ')

    else:
        print(0, end=' ')

'''
/*오답 노트*/
/*느낀 점*/
print(0, end=' ')를 써보고 싶은 적이 있었는데 이번에 쓰게 되어서 나름
기분 좋았다..
'''