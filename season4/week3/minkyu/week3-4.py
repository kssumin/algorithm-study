def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[1])
    flag = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] > flag:
            answer += 1
            flag = routes[i][1]
        else:
            continue
    return answer

"""
풀이
못 풀겠어서 힌트를 봤다.
주제가 그리디라는 것을 알고도 못 풀겠어서 어떻게 푸는지만 봤다.
끝 지점을 기준으로 그냥 계산해주면 된다. 풀고보니 1번 문제랑 똑같다...
근데 이걸 어떻게 생각해내지
"""