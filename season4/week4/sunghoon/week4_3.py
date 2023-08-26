import itertools


def solution(k, dungeons):
    answer = 0

    dun = itertools.permutations(dungeons, len(dungeons))

    for i in dun:
        temp = k
        count = 0

        for a, b in i:
            if temp >= a:
                count += 1
                temp -= b
        answer = max(answer, count)
    return answer