def solution(want, number, discount):
    answer = 0

    for i in range(len(discount) - 9):
        tmp_discount = discount[i:i + 10]
        tmp_bool = [False for _ in range(len(want))]
        for j in range(len(want)):
            if number[j] <= tmp_discount.count(want[j]):
                tmp_bool[j] = True
        if False in tmp_bool:
            pass
        else:
            answer += 1

    return answer