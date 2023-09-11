def solution(n):
    answer = ''
    num_dict = {0: '1', 1: '2', 2: '4'}
    start = 1
    end = 3
    index = 1
    while 1:
        if start <= n <= end:
            break
        else:
            start += 3 ** index
            end += 3 ** (index + 1)
            index += 1

    n -= start
    for i in range(index - 1, 0, -1):
        tmp = n // (3 ** i)
        answer += num_dict[tmp % 3]
    if index >= 2:
        answer += num_dict[n % 3]
    else:
        answer += num_dict[n % 3]

    return answer

"""
풀이
진짜 오래 고민해서 풀었다.
이것도 생각을 잘 해야되는 문제 같다.
그냥 규칙 생각해내서 풀었다.
3진법과 유사하다는데 모르겠다. 어렵다.
"""