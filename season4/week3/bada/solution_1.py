def solution(n, m, section):
    answer = 0
    tmp = 0
    
    for s in section:
        if tmp <= s:
            answer += 1
            tmp = s + m
        else:
            continue
            
    
    return answer