def solution(k, m, score):
    score = sorted(score, reverse=True)
    answer = 0

    for i in range(0, len(score), m):
        box = score[i:i + m]

        if len(box) == m:
            answer += min(box) * m
    return answer