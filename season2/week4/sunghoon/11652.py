'''
/*문제 정보 */
11652번 - 카드
난이도 - 실버 4
/*풀이 방법 */
보유 카드를 입력할 때마다 딕셔너리에  value 값을 올려줘서
최대  value 값을 가진 key 값을 뽑아준다.
'''
import sys
input = sys.stdin.readline

n = int(input()) # 준규가 가지고 있는 카드 수
dic = {}        # 준규 보유 카드딕셔너리

for i in range(n):
    a = int(input())
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

result = sorted(dic.items(), key=lambda x:(-x[1], x[0]))
print(result[0][0])

'''
/*오답 노트*/
/*느낀 점*/
1. result = max(dic, key=dic.get) 처음에 작성하였는데, 도저히 모르겠어서
   검색해보니 정답으로 작성한 코드가 나왔다. 검색을 통해도 저코드가 의미하는 바를 정확히
   잘 모르겠다... 알려주세용..
'''