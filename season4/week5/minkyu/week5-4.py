def solution(book_time):
    answer = 0
    time_table = [0 for _ in range(24 * 60 + 10)]
    for i in range(len(book_time)):
        start, end = book_time[i][0], book_time[i][1]
        start = int(start[0]) * 10 * 60 + int(start[1]) * 60 + int(start[3]) * 10 + int(start[4])
        end = int(end[0]) * 10 * 60 + int(end[1]) * 60 + int(end[3]) * 10 + int(end[4]) + 9

        for i in range(start, end + 1):
            time_table[i] += 1
    answer = max(time_table)
    return answer

"""
풀이
그냥 생각하는대로 푸니까 풀렸다.
방 대실 시간이 제일 많이 겹치는 구간을 구하는 것이 핵심이다.
그런데 처음에 10분 청소시간을 생각하지 않고 풀어서 애 먹었었다. 
"""