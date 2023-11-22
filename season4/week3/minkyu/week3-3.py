from collections import Counter

def solution(k, tangerine):
    answer = 0
    tangerine_dict = Counter(tangerine)
    tangerine = []
    for key, value in tangerine_dict.items():
        tangerine.append([key, value])
    tangerine.sort(key=lambda x: x[1])
    for i in range(len(tangerine) - 1, -1, -1):
        k -= tangerine[i][1]
        answer += 1
        if k <= 0:
            break

    return answer

"""
풀이
처음으로 Counter함수를 사용해봤다. 맨날 까먹는데 전 문제에서도 활용할 수 있던 걸 안 써서 이 문제에서는 써 봤다.
그냥 정렬 문제였다.
"""