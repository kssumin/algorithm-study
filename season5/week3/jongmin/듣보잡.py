# 1764 듣보잡
N,M = map(int, input().split())
not_heared = []
not_saw = []

for _ in range(N):
    not_heared.append(input())

for _ in range(M):
    not_saw.append(input())

not_heared = set(not_heared)
not_saw = set(not_saw)
answer = not_heared.intersection(not_saw)

print(len(answer))
#print(*sorted(list(answer)))
print("\n".join(sorted(list(answer))))