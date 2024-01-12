import sys
#22233번
N,M = map(int,input().split())
keyword = set()
post = []
for _ in range(N):
    keyword.add(sys.stdin.readline().rstrip())

for _ in range(M):
    post.append(sys.stdin.readline().rstrip().split(","))

for i in post:
    for j in i:
        if j in keyword:
            keyword.discard(j)
    print(len(keyword))



