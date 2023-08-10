def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    report = list(set(report))
    report_dict = {}
    id_dict = {}

    for i in range(len(id_list)):
        id_dict[id_list[i]] = i

    for i in range(len(report)):
        a, b = report[i].split()
        report_dict.setdefault(b, 0)
        report_dict[b] += 1

    for i in range(len(report)):
        a, b = report[i].split()
        if report_dict[b] >= k:
            answer[id_dict[a]] += 1

    return answer

"""
풀이
처음 문제를 봤을 때는 어려워보였지만 딕셔너리를 이용했더니 금방 풀렸다.
"""