def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    
    for i in range(0, len(score), m):
        a = score[i:i+m]
        if len(a) == m:
            answer += min(a) * m
            
    return answer
