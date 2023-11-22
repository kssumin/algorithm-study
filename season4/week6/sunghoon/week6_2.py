def solution(s):
    answer = 0

    for i in range(len(s)):
        for j in range(len(s), i, -1):
            a = s[i:j]

            if a == a[::-1]:
                answer = max(answer, len(a))

    return answer