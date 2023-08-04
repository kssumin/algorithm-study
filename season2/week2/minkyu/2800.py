import sys
input = sys.stdin.readline


def BT(N, M):
    if len(result) == M:
        put_list.append(list(result))
        return

    for i in range(1, N):
        if i not in result:
            if not result:
                result.append(i)
                BT(N, M)
                result.pop()
            else:
                if i > max(result):
                    result.append(i)
                    BT(N, M)
                    result.pop()
    return


math_list = input().rstrip()
result = []
# ()순서쌍 만들 때
stack = []
# ()순서쌍의 인덱스 저장할 때
couple = {}
# nCr 조합 넣어놓음
put_list = []
# 내가 출력할 문자열
answer_list = []
count_couple = 0
# ()쌍 찾고 순서 매기고 좌표 저장하기
for i in range(len(math_list)):
    if math_list[i] == '(':
        stack.append(i)
    if math_list[i] == ')':
        a, b = stack.pop(), i
        count_couple += 1
        couple[count_couple] = (a, b)
# answer_result 에 추가
for i in range(1, count_couple + 1):
    BT(count_couple + 1, i)


result_math_list = math_list
for delete_couple_list in put_list:
    for delete_couple in delete_couple_list:
        x, y = couple[delete_couple]
        math_list = list(math_list)
        math_list[x] = "X"
        math_list[y] = "X"
        math_list = ''.join(math_list)
    answer_list.append(math_list.replace("X",""))
    math_list = result_math_list

answer_list = list(set(answer_list))
answer_list.sort()
for answer in answer_list:
    print(answer)
"""
처음 문제를 보고 든 생각
각 ()쌍의 위치를 기억하고 번호를 매겨 리스트에 저장해둔 다음
nCr 조합을 써서 for 문을 써서 nC1, nC2, nC3 ... nCn 개의 ()쌍을 제거한다.
()쌍을 제거한 식은 또 다른 식에 저장해놓고 sort 를 해서 출력한다.
이대로 생각하고 풀었더니 잘 풀렸다.

생겼던 문제점
1. 얕은 복사를 해서 BT 함수를 써서 조합식을 저장할 때 다 빈 리스트로 저장이 되었다.
(예전에 이차원 배열을 만들 때도 얕은 복사를 해서 안됐던 기억이 있는데 객체 공부를 좀 더 해야겠다.)
2. 입력 받은 값은 문자열이고 문자열은 인덱싱이 가능하니까 그 문자열은 수정이 가능하다고 생각했는데 수정이 불가능했다.
그래서 그 문자열을 리스트로 형변환해주고 수정하고 싶은 부분을 수정하고 다시 str 로 형변환하려고 했는데 안됐다. 그래서 ''.join 을 사용했다.
3. 왜인지 모르겠는데 틀렸다고 나왔다. 도저히 모르겠어서 반례를 봤는데 ((1)) 같이 한 숫자를 여러 개의 괄호로 묶으면 중복값을 출력해서 틀렸다고 뜬다.
그래서 set 로 중복을 없애줬다.

풀이
10799번 문제(레이저 문제)를 풀 때 stack 으로 푼 풀이를 참고해서 ()쌍을 판별하고 번호와 매기고 좌표를 저장해서 couple 에 저장한다. ()가 몇 개 있는지도
중요하므로 ()의 개수도 count_couple 에 저장해준다. 그리고 예전에 nCr 조합을 만들었던 게 기억이 나서 그 코드를 참고해서 BT 함수를 만들었다. 그 결과들은 put_list 에 저장한다.
그리고 ()들을 하나 하나씩 X로 바꾸었다가 X를 없애고 answer_list 에 append 한다.
중복값을 제거한 뒤 sort 해서 출력한다.


"""
