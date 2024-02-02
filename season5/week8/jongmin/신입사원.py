T = int(input())
answer = []

for i in range(T):

    N = int(input())
    applicant = []
    cnt = 0

    for j in range(N):
        applicant.append(list(map(int, input().split())))

    applicant.sort(key=lambda x:x[0])

    minimum = applicant[0]

    for j in applicant:
        if minimum[1] >= j[1]:
            cnt += 1
            minimum = j
        
    answer.append(cnt)

for i in answer:
    print(i)