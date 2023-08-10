def solution(k, m, score):
    answer = 0
    score.sort()
    while 1:
        if len(score) >= m:
            for i in range(m):
                if i == m-1:
                    min_num = score.pop()
                else:
                    score.pop()
            answer += min_num * m
        else:
            break
    return answer

"""
풀이
그냥 정렬 문제였다. 정렬만 하면 쉽게 풀린다.
"""