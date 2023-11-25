from collections import Counter


def solution(str1, str2):
    answer = 0
    st1 = []
    st2 = []
    for i in range(len(str1) - 1):
        a = str1[i:i + 2]
        if a.isalpha():
            st1.append(a.lower())

    for i in range(len(str2) - 1):
        a = str2[i:i + 2]
        if a.isalpha():
            st2.append(a.lower())
    Counter1 = Counter(st1)
    Counter2 = Counter(st2)

    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)

    return st1