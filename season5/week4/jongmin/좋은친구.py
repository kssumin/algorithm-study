from itertools import combinations as comb

N,K = map(int, input().split())

students = []
bestFriends = set()

for i in range(N):
    students.append(input())

for i in range(N-K):
    #print(tmp)
    for j in list(comb(students[i:i+K+1],2)):
        bestFriends.add(j)

#print(*bestFriends)
cnt = 0
for i in bestFriends:
    if len(i[0]) == len(i[1]):
        cnt+=1

print(cnt)