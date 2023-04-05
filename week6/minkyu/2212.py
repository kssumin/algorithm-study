import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
if N < K:
    print(0)
    exit(0)
sensor = sorted(list(map(int, input().split())))
distance = []
for i in range(N - 1):
    distance.append(sensor[i + 1] - sensor[i])
distance.sort()
for _ in range(K - 1):
    distance.pop()
print(sum(distance))

"""
풀이
처음에 문제도 이해가 안 가서 이해하는데에 오래 걸렸다.
일단 각 좌표를 sensor에 저장한 후 sensor에 저장된 순서대로 좌표끼리의 거리를 distance에 저장한다.
그리고 이 거리 중 큰 순서대로 K - 1개 제거하고 더하면 정답이다.

index에러가 떠서 왜그런지 못 찾겠어서 찾아봤는데 N<K일 때 pop할 게 없어서 오류가 뜬다.
K가 N보다 클 때 N = K를 해도 되지만 N<K일 떄 어차피 결과가 0이니까 밑에 코드를 지나칠 필요 없이 print(0)하고 exit(0)하기로 했다.
"""