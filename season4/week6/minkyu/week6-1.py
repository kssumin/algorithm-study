def solution(park, routes):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct_dict = {'E': 0, 'S': 1, 'W': 2, 'N': 3}

    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                start_x, start_y = i, j

    for i in range(len(routes)):
        direct, dist = routes[i].split()
        dist = int(dist)
        origin_x, origin_y = start_x, start_y
        for j in range(1, dist + 1):
            start_x += dx[direct_dict[direct]]
            start_y += dy[direct_dict[direct]]
            if not (0 <= start_x < len(park)) or not (0 <= start_y < len(park[0])) or park[start_x][start_y] == 'X':
                start_x, start_y = origin_x, origin_y
                break

    return [start_x, start_y]

"""
풀이
그냥 하라는대로 해서 풀었다.
맨날 조건을 대충봐서 한번씩은 틀린다.
조건을 자세히 봐야겠다.
"""