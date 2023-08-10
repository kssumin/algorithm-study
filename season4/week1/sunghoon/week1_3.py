def solution(cards):
    answer = []
    for i in range(len(cards)):
        count = 0

        while cards[i]:
            a = cards[i] - 1
            count += 1
            cards[i] = 0
            i = a
        answer.append(count)
        answer.sort(reverse=True)
    return answer[0] * answer[1]