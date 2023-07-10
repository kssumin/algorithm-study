'''
/*문제 정보 */
20529번 - 가장 가까운 세 사람의 심리적 거리
난이도 - 실버 1
/*풀이 방법 */
조합을 이용해 거리 수를 계산해주었다.
계속 오답이 나와 나와 같이 조합을 이용한 블로그를 찾아봤다.
'''
from itertools import combinations
import sys
input = sys.stdin.readline

mbtis = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ',
         'ISTP', 'ISFP', 'INFP', 'INTP',
         'ESTP', 'ESFP', 'ENFP', 'ENTP',
         'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']

t = int(input())
for i in range(t):
    table = {mbti: 0 for mbti in mbtis}
    n = int(input())
    temp = input().split()
    if n > 32:     # 비둘기집 원리 32개의 mbti 가 모이면 무조건 같은 3개가 나옴
        print(0)
        continue
    else:
        for mbti in temp:
            table[mbti] += 1     # mbti 딕셔너리에서 3인 값 있는지 확인
            if table[mbti] == 3:
                print(0)
                break
        else:
            temp = list(combinations(temp, 3))
            score_list = []
            for comb in temp:
                score = 0
                for i in range(4):
                    if (comb[0][i] == comb[1][i] and
                            comb[0][i] == comb[2][i] and
                            comb[1][i] == comb[2][i]):
                        score += 0
                    else:
                        score += 2
                score_list.append(score)
            print(min(score_list))

'''
/*오답 노트*/ 
오답 1. 메모리 초과
from itertools import combinations
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    li = list(input().split())

    a = list(combinations(li,3))
    result = []
    for comb in a:
        count = 0
        for i in range(4):
            if(comb[0][i] == comb[1][i]) and (comb[0][i] == comb[2][i]) and (comb[1][i] == comb[2][i]):
                count += 0

            else:
                count += 2
        result.append(count)

print(min(result))

오답 2. 런타임 에러
    if n > 32:
        print(0)
        continue
    오답 1에 위의 조건문을 넣으니 런타임 에러가 떴다.
    
/*느낀 점*/
이 문제를 풀때, 일반적으로 구하는 방법만 찾아 메모리초과가 나왔다.
검색해서 비둘기집원리로 n >32 이 일 때 조건을 주어서 줄였지만
32보다 작을 때도 3개가 나오는 경우를 따로 할 생각을 하지 않았다.
코딩 너무 어려워.. 문제의 경우의 수를 찾는 것도 문제고 그걸 코딩하는 것도
귀찮거나 어려운 것도 문제다..
'''