def solution(today, terms, privacies):
    answer = []
    y, m, d = today.split('.')
    today_to_day = int(y) * 12 * 28 + int(m) * 28 + int(d)
    terms_dic = {}

    for i in terms:
        a = i.split(" ")
        terms_dic[a[0]] = int(a[1]) * 28

    for i in range(len(privacies)):
        first = privacies[i].split(" ")
        second = first[0].split('.')

        change_day = int(second[0]) * 12 * 28 + int(second[1]) * 28 + int(second[2]) + terms_dic[first[1]]
        if today_to_day >= change_day:
            answer.append(i + 1)

    return answer