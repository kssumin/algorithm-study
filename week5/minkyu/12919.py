import sys
input = sys.stdin.readline


def BT(letter):
    global answer
    if letter == result:
        answer = 1
        return
    if len(letter) < len(result):
        return
    if letter[0] == "B":
        BT(letter[:0:-1])
    if letter[-1] == "A":
        BT(letter[:len(letter) - 1:])


S = input().rstrip()
T = input().rstrip()

len_S = len(S)
len_T = len(T)
if len_S == len_T:
    print(0)
else:
    if len_S > len_T:
        target, result = S, T
    else:
        target, result = T, S
    answer = 0
    BT(target)
    print(answer)

"""
풀이
처음엔 백트래킹으로 푼 줄 알았지만 dfs로 푼 것 같다.
global 쓰는 걸 별로 안 좋아하는데 안 쓰면 비효율적일 거 같아 어쩔 수 없이 사용했다. ㅠ
다른 사람 풀이를 보니 return true를 하고 if문에 조건과 함께 and 재귀함수를 했다. 아니면 정답일 때는 exit(0)을 해서 강제종료하기도 했다.

문제상황 그대로 하면 경우의 수가 너무 많아질 거 같아 조건을 거꾸로 바꾸어서 큰 문자열을 줄이는 것으로 바꾸었다.
그렇게 바꾸면 조건 1 문자열[0] == B일 때 문자열을 거꾸로 바꾼 후 마지막 문자 삭제
            조건 2 문자열[-1] == A일 때 마지막 문자 삭제, 조건에 맞지 않으면 만들 수 있는 가능성이 없다.
"""