def solution(weights):
    answer = 0
    weights_dict = {}
    for i in range(len(weights)):
        weights_dict.setdefault(weights[i], 0)
        weights_dict[weights[i]] += 1

    for key, value in weights_dict.items():
        if value >= 2:
            answer += value * (value - 1) // 2
        if key * 2 in weights_dict:
            answer += value * weights_dict[key * 2]
        if key * 3 % 2 == 0 and key * 3 // 2 in weights_dict:
            answer += value * weights_dict[key * 3 // 2]
        if key * 4 % 3 == 0 and key * 4 // 3 in weights_dict:
            answer += value * weights_dict[key * 4 // 3]

    return answer


"""
풀이
처음에 조합을 이용해서 전체탐색으로 풀었는데 시간초과가 떴다.
그 다음에 그냥 이중포문으로 전체탐색을 했는데 1문제 더 맞히고 또 시간초과가 떴다.
그래서 set나 dict로 풀어야겠다고 생각했다.
dict에 각 숫자가 몇 개인지 저장한다. 각 숫자에 2,3/2,4/3배 했을 때의 숫자가 몇 개 있는지도 구하고
그 두 숫자끼리 곱한다.
"""