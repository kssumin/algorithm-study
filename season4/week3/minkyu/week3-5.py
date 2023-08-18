def solution(jobs):
    jobs.sort(key=lambda x: (x[0], x[1]))
    jobs_len = len(jobs)

    end = jobs[0][0] + jobs[0][1]
    total = jobs[0][1]
    jobs.pop(0)
    jobs.sort(key=lambda x: (x[1], x[0]))

    now_len = len(jobs)
    rotate_num = 0
    while jobs:
        if not jobs:
            break
        if rotate_num == now_len:
            jobs.sort(key=lambda x: (x[0], x[1]))
            end = jobs[0][0] + jobs[0][1]
            total += jobs[0][1]
            jobs.pop(0)
            now_len -= 1
            jobs.sort(key=lambda x: (x[1], x[0]))
        if jobs[0][0] > end:
            jobs.append(jobs.pop(0))
            rotate_num += 1
        else:
            end += jobs[0][1]
            total += end - jobs[0][0]
            jobs.pop(0)

    answer = total // jobs_len
    return answer

"""
풀이
처음에 큐를 써야할 것 같아서 큐를 썼는데 큐를 쓰면 정렬 함수를 쓸 수 없다...
그래서 그냥 리스트를 쓰는데 큐처럼 썼다.
이 문제는 걸리는 시간이 적은 작업을 먼저 처리해야한다.
그런데 무작정 걸리는 시간이 적은 작업을 해버리면 작업 요구 시간 이전에 작업을 해버릴 수 있다..
그래서 예외를 잘 생각해서 풀면 풀린다.
"""