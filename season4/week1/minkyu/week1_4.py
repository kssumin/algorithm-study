def solution(cards):
    answer = 0
    box_open = [False for _ in range(len(cards))]
    box_list = [0 for _ in range(len(cards))]
    box_count = 0
    for i in range(len(cards)):
        if not box_open[i]:
            box_open[i] = True
            index = cards[i] - 1
            while 1:
                box_list[box_count] += 1
                if not box_open[index]:
                    box_open[index] = True
                    index = cards[index] - 1
                else:
                    box_count += 1
                    index = cards[index] - 1
                    break

    box_list.sort()
    answer = max(box_list[-1] * box_list[-2], answer)

    return answer

"""
풀이
유튜브에서 비슷한 문제를 본 기억이 있어서 루프가 중요하고 어디서 시작하든 루프의 개수는 동일하다는 것을 알고 있었다.
그래서 루프를 만들고 정렬해서 그 개수가 젤 많은 것 두 개를 곱해서 정답을 맞췄다.
"""