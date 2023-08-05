'''
/*문제 정보 */
9996번 - 한국이 그리울 땐 서버에 접속하지
난이도 - 실버 3
/*풀이 방법 */
주어진 패턴의 인덱스만큼 문자열 앞 뒤에서 빼와 비교를 해주었다.
'''
import sys
input = sys.stdin.readline

n = int(input())

s, e = input().split('*')

for _ in range(n):
    l = input()


    if s == l[:len(s)] and e == l[-len(e):] and len("".join(s + e)) <= len(l):
        print("DA")

    else:
        print("NE")


'''
/*오답 노트*/
1. s, e = map(str, input().rstrip().split("*"))
에서 rstrip 을 적어주지 않아 예제를 넣었을 때, DA 가 적히지 않았다.

2.   if s == l[0] and e == l[-1]:
        print("DA")
    에제와 다르게 * 앞뒤로 알파벳이 여러개 오는 경우를 생각하지 않았다.

/*느낀 점*/
처음에는 패턴이 알파벳 한개 씩인 경우만 생각해서 오답나왔다가 여러개인 경우를 생각해서
인덱스 만큼 문자열에서 빼내오는 것이 조금 복잡했다.
'''