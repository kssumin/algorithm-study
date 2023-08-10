INF = 15

def solution(s):
    count_zero = 0
    count_solution = 0
    while 1:
        count_solution += 1
        count_zero += s.count('0')
        s = s.replace('0', '')
        num = len(s)
        start = 0
        end = INF
        while end >= start:
            mid = (start + end) // 2
            if 2 ** mid > num:
                end = mid - 1
            else:
                start = mid + 1
        start -= 1

        new_num = ''
        while start != -1:
            if num >= 2 ** start:
                new_num += '1'
                num -= 2 ** start
            else:
                new_num += '0'
            start -= 1
        s = new_num

        if s == '1':
            break
    answer = [count_solution, count_zero]

    return answer
