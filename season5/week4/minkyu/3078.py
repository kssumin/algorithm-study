import sys
input = sys.stdin.readline

N, K = map(int, input().split())
friends = []
result = 0
len_dict = dict()
for i in range(2, 21):
    len_dict[i] = 0

for i in range(N):
    friends.append(len(input().rstrip()))

for i in range(1, K + 1):
    if i >= N - 1:
        break
    len_dict[friends[i]] += 1


for i in range(1, N):
    start = i
    end = i+K-1

    result += len_dict[friends[start-1]]

    if end >= N - 1:
        end = N - 1
    len_dict[friends[start]] -= 1
    if end + 1 < N:
        len_dict[friends[end+1]] += 1

print(result)