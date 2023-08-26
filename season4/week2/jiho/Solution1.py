def solution(n, m, section):
    answer = 1
    start = section[0] 
    for i in range(1, len(section)):
        if section[i] - start >= m:
            answer += 1
            start = section[i]
    return answer