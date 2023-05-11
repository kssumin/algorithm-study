'''
/*문제 정보 */
1789번 - 수들의 합
난이도 - 실버 5
/*풀이 방법 */
1부터 차례대로 더해주다가 입력된 s보다 커질 때, n-1를 출력해준다.

'''
import sys
input = sys.stdin.readline

s = int(input())
count = 0
sum1 = 0

while 1:
    count += 1
    sum1 += count

    if sum1 > s:
        break
print(count - 1)

'''
/*오답 노트*/
/*느낀 점*/
주제에 너무 집중해서 이분탐색으로 푸는데 난이도에 비해 너무 복잡해져서
서치를 해보니 간단한 공식으로 푸는 문제였다..
'''