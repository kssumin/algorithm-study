'''
/*문제 정보 */
19637번 - IF문 좀 대신 써줘
난이도 - 실버 3
/*풀이 방법 */
https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-19637-IF%EB%AC%B8-%EC%A2%80-%EB%8C%80%EC%8B%A0-%EC%8D%A8%EC%A4%98-Binary-Search
코드리뷰 했습니다.
이진 탐색을 쉽게 구현할 수 있는 bisect 라이브러리를 사용하였습니다.
'''
import sys
from bisect import bisect_left
input = sys.stdin.readline

n, m = map(int, input().split())
title = []
power = []

for _ in range(n):
    a, b = input().split()
    title.append(a)
    power.append(int(b))

for _ in range(m):
    print(title[bisect_left(power, int(input()))])


'''
/*오답 노트*/
/*느낀 점*/
처음에 문제를 봤을 때, 칭호와 전투력을 따로 저장해놓을 생각을 하지 못했다.
너무 멍청한 것 같다... 
'''