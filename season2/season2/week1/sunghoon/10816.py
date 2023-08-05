'''
/*문제 정보 */
10816번 - 숫자 카드 2
난이도 - 실버 4
/*풀이 방법 */
상근이랑 가지고 있는거랑 개수를 찾아야하는 것을 따로 저장해 주었다.
처음에는 반복문으로 돌려서 하나하나 카운트 하려 했는데 복잡해져서 찾아보니
collections 모듈 counter를 알게 되어서 그걸로 풀게 되었다.
'''
from collections import Counter

n = int(input())
sanggun =list(map(int, input().split()))

m = int(input())
quest = list(map(int, input().split()))

a = Counter(sanggun)

for i in quest:
    if i in a:
        print(a[i], end = " ")

    else:
        print(0, end = " ")


'''
/*오답 노트*/
/*느낀 점*/
주어진 값을 리스트로 받을 때 처음에는 for 문으로 하나하나 받으려 했는데
깔끔하게 list(map(int, input().split()))로 받아 주었다. 
'''