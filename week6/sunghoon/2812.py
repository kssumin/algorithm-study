'''
/*문제 정보 */
2812번 - 크게 만들기
난이도 - 골드 3
/*풀이 방법 */
도저히 어떻게 풀어야할 지 모르겠어서 풀이 리뷰를 했다.!
https://ryu-e.tistory.com/76
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = input().rstrip()    # 나는 int 로 받았었는데 굳이 그럴 필요가 없는 것 같다.

st = list()   # stack 만들어주기
for i in range(n):
    while st and k > 0 and st[-1] < s[i]:    # 제거해야하는 횟수가 남아있고 리스트에 담은 값이 현재 숫자보다 작으면
        st.pop()             # 이전에 담은 수는 제거
        k -= 1               # 제거 횟수 -1
    st.append(s[i])          # 현재 숫자 담아주기

print("".join(st[:len(st) - k]))   # 나타내줘야하는 만큼 나타내주기
'''
/*오답 노트*/
/*느낀 점*/
다른 사람드의 풀이를 보니 너무 어렵게 생각하고 있었던 것 같다. 반복문 조건 걸어주면서
k 횟수 조절하면 되는 문제였다..
'''