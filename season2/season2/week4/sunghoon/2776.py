'''
/*문제 정보 */
2776번 - 암기왕
난이도 - 실버 4
/*풀이 방법 */
note1과 note2 를 받고 있을 때 1, 없을 때 0 나타내줌.
'''
import sys
input = sys.stdin.readline

t = int(input())    # 테스트 케이스
for _ in range(t):

    n = int(input())    # 수첩 1에 적어 놓은 정수의 개수
    note1 = set(map(int, input().split()))

    m = int(input())    # 수첩 1에 적어 놓은 정수의 개수
    note2 = list(map(int, input().split()))

    for i in range(m):
        if note2[i] in note1:
            print(1)
        else:
            print(0)


'''
/*오답 노트*/
/*느낀 점*/
1. set 과 list 의 차이를 정확히 공부해야 할 것 같다.
   예제에서는 note1에 대해 중복값이 없어서 생각 못 했는데
   list를 쓰니 바로 시간초과가 나왔다. 둘의 차이를 제대로
   알아봐야겠다.
'''