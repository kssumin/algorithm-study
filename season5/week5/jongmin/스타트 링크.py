from itertools import combinations, permutations

N = int(input())
arr = []
comb = set(list(combinations(range(0,N),N//2)))
mem_set = set(range(0,N))
results = set()
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in comb:
    #print(i)
    score_start = 0
    score_link = 0
    for j,k in list((combinations(i,2))):
        score_start += arr[j][k]
        score_start += arr[k][j]

    for j,k in list(combinations(mem_set.difference(i),2)):
        score_link += arr[j][k]
        score_link += arr[k][j]
    
    results.add(abs(score_start-score_link))

print(min(results))
    