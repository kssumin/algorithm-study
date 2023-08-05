'''
/*문제 정보 */
19941번 - 햄버거 분배
난이도 - 실버 3
/*풀이 방법 */
리스트에서 p가 나올 경우 양쪽 k 만큼의 거리 중 가장 왼쪽에 있는 햄버거를 선택하는 방식으로
카운트 해주었다.  반복문에서 인덱스 에러가 생길 것을 대비해 0을 k 만큼 입력값에 붙여
새로운 리스트로 반복문을 돌려주었다.
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(input().rstrip())
arr2 = [0] * k
arr3 = arr2 + arr + arr2

count = 0
for i in range(len(arr3)):
    if arr3[i] == 'P':
        for j in range(i-k, i+k+1,1):
            if arr3[j] == 'H':
                arr3[j] = 0
                count += 1
                break
print(count)

'''
/*오답 노트*/
에제 1은 맞게 나왔는데 예제 2가 틀려 잘못된 부분을 찾아보니, 
for i in range(n)): 을 해주었었다. 앞 뒤로 0을 붙혔으니 
n 자리에 len(arr3)을 넣었어야 했다.
/*느낀 점*/
그냥 생각하는 대로 적은게 풀려 주제가 무엇인지 찾아보니 그리디 였다.
'''