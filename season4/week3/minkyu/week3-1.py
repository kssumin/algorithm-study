def solution(n, m, section):
    answer = 1
    flag = section[0] + m - 1
    for i in range(len(section)):
        if section[i] <= flag:
            continue
        else:
            flag = section[i] + m - 1
            answer += 1
    return answer

"""
풀이
그냥 생각하는대로 푸니까 풀렸다.
항상 변수 이름 짓는게 어렵다.
"""