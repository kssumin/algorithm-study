from collections import deque

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]
    result = []
    for i in range(len(roads)):
        start, end = roads[i][0], roads[i][1]
        graph[start].append(end)
        graph[end].append(start)

    distance = [-1 for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    queue = deque([[destination, 0]])
    while queue:
        q, dist = queue.popleft()
        if not visited[q]:
            visited[q] = True
            distance[q] = dist
            for j in range(len(graph[q])):
                queue.append([graph[q][j], dist + 1])
    for i in range(len(sources)):
        result.append(distance[sources[i]])
    """
    for i in range(len(sources)):
        visited = [False for _ in range(n + 1)]
        queue = deque([[sources[i], 0]])
        while queue:
            q, dist = queue.popleft()
            if q == destination:
                result.append(dist)
                break
            if not visited[q]:
                visited[q] = True
                for j in range(len(graph[q])):
                    queue.append([graph[q][j], dist + 1])
        else:
             result.append(-1)
    """
    return result


"""
풀이
처음에 그냥 bfs로 했는데 시간초과가 떴다.
처음에 부대원들이 도착지까지 걸리는 시간을 계산하는 식을 짰었는데
알고보니 반대로 도착지부터 각 지역까지의 거리를 구해야됐다.
각 지역에서 도착지까지의 거리를 구하면 되니 각 지역으로 for문을 돌릴게 아니라 도착지부터 각 지역까지의 거리를 구하면 되는것이였다.
역시 잘 안풀리면 역으로 생각하면 된다. 항상 알고는 있는데 생각은 잘 못한다... ㅠ 
"""
