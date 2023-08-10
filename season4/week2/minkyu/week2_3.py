from collections import deque


def solution(s):
    answer = 0
    q = deque(s)
    dict_close = {'[': ']', '(': ')', '{': '}'}

    for j in range(len(s) - 1):
        tmp = deque([])
        for i in range(len(s)):
            tmp.append(q[i])
            while 1:
                if len(tmp) >= 2 and tmp[-2] in dict_close:
                    if tmp[-1] == dict_close[tmp[-2]]:
                        tmp.pop()
                        tmp.pop()
                    else:
                        break
                else:
                    break
        if not tmp:
            answer += 1
        q.rotate(-1)

    return answer