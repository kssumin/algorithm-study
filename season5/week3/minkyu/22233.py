import sys
input = sys.stdin.readline

N, M = map(int, input().split())
note = set()
for i in range(N):
    note.add(input().rstrip())
for i in range(M):
    for keyword in input().rstrip().split(","):
        if keyword in note:
            note.remove(keyword)
            N -= 1
    print(N)