def solution(n, times):
    answer = 0
    start, end = 1, max(times) * n
    while start <= end:
        mid = (start + end) // 2
        people = 0
        for i in range(len(times)):
            people += mid // times[i]
        if people >= n:
            end = mid - 1
        else:
            start = mid + 1
    answer = start
    return answer

"""
풀이
저번에 풀었던 기억이 있었는데도 푸는데 시간이 꽤 걸렸다
또 문제를 풀기 전에 알고리즘 주제가 이분탐색이라는 것을 알았는데도 시간이 걸렸다!!!
반성해야겠다. 그래도 풀었던 기억 때문에 시간이 엄청 걸리진 않았다
"""