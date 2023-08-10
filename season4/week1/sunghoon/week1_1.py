def solution(x, n):
    answer = []
    i = 0
    while len(answer) < n:
        i += x
        answer.append(i)

    return answer