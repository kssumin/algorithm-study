import sys
input = sys.stdin.readline


def is_right():
    N = int(input())
    note_1 = set(map(int, input().split()))

    M = int(input())
    note_2 = list(map(int, input().split()))

    for num in note_2:
        if num in note_1:
            print(1)
        else:
            print(0)
    return


T = int(input())
for i in range(T):
    is_right()


"""
풀이
노트 1에 있는 숫자는 중복이 있든 없든 상관 없기 때문에 set로 선언해준다.
그리고 노트 2에 있는 숫자 순서대로 결과를 출력해야하기 때문에 노트 2는 리스트로 선언해준다.
"""