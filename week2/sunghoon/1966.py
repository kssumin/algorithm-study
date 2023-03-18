'''
/*문제 정보 */
1966번 - 프린터 큐
난이도 - 실버 3
/*결과*/
메모리 - 31256KB
시간 - 52ms
코드 길이 - 1134B
/*풀이 방법 */
굳이 큐를 사용하지 않아도 될 것 같아 리스트를 사용
중요도와 대상의 인덱스를 따로 따로 저장하여 반복문으로 풀어줌.
'''
import sys
a = int(sys.stdin.readline())  # a는 테스트케이스의 수

for i in range(a):  # 테스트케이스 시작
    n, m = map(int, sys.stdin.readline().split())  # 문서의 개수 n, 궁금한 대상 m

    x = list(sys.stdin.readline().split())   # 중요도를 받아서 리스트에 넣어줌
    y = [0 for i in range(n)]  # 대상의 위치 저장할 리스트 생성
    y[m] =1                    # 대상의 위치 값만 1로 바꿈
    count = 0   # 문서가 몇 번 나갔는지 카운트
    while True:

        if x[0] == max(x):
            count +=1       # 맨 앞의 값이 최댓값이면 빠져나가니 count +1 해줌
            if y[0] == 1:
                print(count)    # 거기다 만약 그 값이 우리가 찾는 대상이면 종료
                break

            else:              # 우리가 찾는 대상이 아니면 제거하고 계속 반복
                del x[0]
                del y[0]

        else:
            x.append(x[0])
            y.append(y[0])
            del x[0]
            del y[0]          # 맨 앞 값이 최대값이 아니면 순서 뒤로 빼주기


'''
/*오답 노트*/
/*느낀 점*/
1. 큐로 푸려다가 생각해보니 리스트도 가능하고 편할 것 같아 리스트로 사용
2. 처음에 대상의 인덱스를 따로 저장하지 않았었는데 
    y = [0 for i in range(n)]  # 대상의 위치 저장할 리스트 생성
    y[m] =1                    # 대상의 위치 값만 1로 바꿈
    이 아이디어 그 뒤에는 쉽게 풀 수 있었다...
'''