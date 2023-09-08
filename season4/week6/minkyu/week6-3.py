from collections import deque

def make(word):
    result = []
    tmp = ""
    word = deque(word)
    while word:
        tmp += word.popleft()
        if len(tmp) == 2:
            if tmp.isalpha():
                result.append(tmp.upper())
                tmp = tmp[1:]
            else:
                tmp = tmp[1:]
    return result


def solution(str1, str2):
    answer = 0
    str1 = make(str1)
    str2 = make(str2)
    if not str1 and not str2:
        return 65536
    up = 0
    down = 0
    word_set = set(str1) | set(str2)
    for words in word_set:
        up += min(str1.count(words), str2.count(words))
        down += max(str1.count(words), str2.count(words))
    answer = int(up / down * 65536)

    return answer

"""
풀이
합집합과 교집합을 이용해서 풀었다.
"""